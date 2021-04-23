import streamlit as st
import time
import pandas as pd

import findspark
findspark.init()
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import HashingTF, StopWordsRemover, Tokenizer
from pyspark.sql import SparkSession
import pyspark.sql.functions as spark_funcs

def app():
    # st.set_page_config(layout="wide")
    st.title('Product Analysis')
    st.write('Welcome to Positive Products')

    st.write(
    """_Uploaded files must contain the following column which must be labeled in the first row of the file_\n
    `Review`
    """)
    fp = st.file_uploader('Upload JSON')
    
    if fp is not None:
        
       with st.spinner('Processing...'):
            st.success('File uploaded Successfully!')

   


    

    selection = st.selectbox("Select a model to process data:",("CD and Vinyl", "Digital Music","Pet Supplies","Industrial and Scientific","Arts and Craft"))
    
    if selection =="CD and Vinyl":
        lr_model = LogisticRegressionModel.load('../models/model1.dat')
    if selection =="Digital Music":
        lr_model = LogisticRegressionModel.load('../models/model2.dat')
    if selection =="Pet Supplies":
        lr_model = LogisticRegressionModel.load('../models/model3.dat')
    if selection =="Industrial and Scientific":
        lr_model = LogisticRegressionModel.load('../models/model4.dat')
    if selection =="Arts and Craft":
        lr_model = LogisticRegressionModel.load('../models/model5.dat')
    
    if st.button("Start Analysis"):
        with st.spinner('Processing...'):
            # call model functions here
            time.sleep(3)
            st.header("Top Reviewed Products")
            c1, c2, c3 = st.beta_columns((1, 1, 2))
            c1.subheader("**Product**")
            c2.subheader("**Overall Sentiment Score**")
            c3.subheader("**Meaningful Words**")
            for x in range(6):
                c1.write('Product #')
                c1, c2, c3 = st.beta_columns((1, 1, 2))
    
        