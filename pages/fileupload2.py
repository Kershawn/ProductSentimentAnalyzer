from collections import Counter

import pandas as pd

import findspark
findspark.init()
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import HashingTF, StopWordsRemover, Tokenizer
from pyspark.sql import SparkSession
import pyspark.sql.functions as spark_funcs
import streamlit as st
import streamlit_wordcloud as wc

spark = SparkSession.builder.master('local[*]').appName('Big Data Project').getOrCreate()
st.write('# Sentiment Analyzer')
fp = st.file_uploader('Upload CSV')
st.write(
"""_Uploaded files must contain at least the followings column which must be labeled in the first row of the file_\n
`Review`, `Product_Name`
""")
lr_model1 = LogisticRegressionModel.load('../models/model1.dat')
# lr_model2 = LogisticRegressionModel.load('../models/model2.dat')
# lr_model3 = LogisticRegressionModel.load('../models/model3.dat')
# lr_model4 = LogisticRegressionModel.load('../models/model4.dat')
# lr_model5 = LogisticRegressionModel.load('../models/model5.dat')


def load_data(fp):
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

def get_word_clouds(product_summary):
    products = product_summary.index
    for prod in products:
        words = product_summary['Cleaned_Reviews'][prod].split()
        ctr = Counter(words)
        wcdict = [{'text': w, 'value': c} for w, c in ctr.items()]
        st.subheader(f'Top words for Product: {prod}')
        wcloud = wc.visualize(wcdict)


if fp is not None:
    df = load_data(fp)
    df = clean_data(df)
    df = tokenize_data(df)
    dff = predict_sentiment(df, lr_model1)
    dfp = dff.toPandas().head(100)
    product_summary = dfp.groupby('Product_Name').agg({'prediction': 'mean', 'Cleaned_Reviews': lambda x: ' '.join((' '.join(i) for i in x))})
    product_summary['Sentiment'] = product_summary['prediction']
    st.subheader('Top products')
    top_products = product_summary.sort_values(by=['Sentiment'], ascending=False).head(10)
    st.write(top_products[['Product_Name', 'Sentiment']])
    get_word_clouds(top_products)
    st.subheader('Bottom products')
    bottom_products = product_summary.sort_values(by=['Sentiment']).head(10)
    st.write(bottom_products[['Product_Name', 'Sentiment']])
    get_word_clouds(bottom_products)
