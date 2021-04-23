import pandas as pd

import findspark
findspark.init()
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import HashingTF, StopWordsRemover, Tokenizer
from pyspark.sql import SparkSession
import pyspark.sql.functions as spark_funcs
import streamlit as st

spark = SparkSession.builder.master('local').appName('Big Data Project').getOrCreate()
lr_model1 = LogisticRegressionModel.load('../models/model1.dat')
lr_model2 = LogisticRegressionModel.load('../models/model2.dat')
lr_model3 = LogisticRegressionModel.load('../models/model3.dat')
lr_model4 = LogisticRegressionModel.load('../models/model4.dat')
lr_model5 = LogisticRegressionModel.load('../models/model5.dat')

st.write('# Sentiment Analyzer')
fp = st.file_uploader('Upload CSV')
st.write(
"""_Uploaded files must contain at least the followings column which must be labeled in the first row of the file_\n
`Review`, `Product_Name`
""")


def load_data():
    return spark.createDataFrame(pd.read_csv(fp))


def clean_data(df):
    data = df.select('Review', 'Product_Name')
    data = data.withColumn('Review', spark_funcs.regexp_replace(spark_funcs.col('Review'), '[^\w\s]', ''))
    data = data.withColumn('Review', spark_funcs.regexp_replace(spark_funcs.col('Review'), 'r[\d+\s]', ''))
    data = data.withColumn('Review', spark_funcs.regexp_replace(spark_funcs.col('Review'), '[^a-zA-Z\\s]', ''))
    data = data.filter(data.Review.isNotNull())
    data = data.withColumn('Review', spark_funcs.lower(spark_funcs.col('Review')))
    return data


def tokenize_data(df):
    tokenizer = Tokenizer(inputCol='Review', outputCol='Review_Tokens')
    data = tokenizer.transform(df).select('Review', 'Product_Name', 'Review_Tokens')
    remover = StopWordsRemover(inputCol='Review_Tokens', outputCol='Cleaned_Reviews')
    data = remover.transform(data).select('Review', 'Product_Name', 'Review_Tokens', 'Cleaned_Reviews')
    return data


def predict_sentiment(df, model):
    hashTF = HashingTF(inputCol='Cleaned_Reviews', outputCol='features')
    numericTest = hashTF.transform(df).select('Product_Name', 'Cleaned_Reviews', 'features')
    prediction = model.transform(numericTest)
    data = prediction.select('Cleaned_Reviews', 'prediction', 'Product_Name')
    return data


if fp is not None:
    df = load_data()
    df = clean_data(df)
    df = tokenize_data(df)
    dff = predict_sentiment(df, lr_model1)
    st.write(dff.toPandas())
    dff = predict_sentiment(df, lr_model2)
    st.write(dff.toPandas())
    dff = predict_sentiment(df, lr_model3)
    st.write(dff.toPandas())
    dff = predict_sentiment(df, lr_model4)
    st.write(dff.toPandas())
    dff = predict_sentiment(df, lr_model5)
    st.write(dff.toPandas())
