import streamlit as st
import time
import pandas as pd

import findspark
findspark.find()
findspark.init()
from pyspark.ml.classification import LogisticRegressionModel

from pages.fileupload2 import main


def app(spark):
    # st.set_page_config(layout="wide")
    st.title('Product Analysis')
    st.write('Welcome to Positive Products')

    st.write(
    """_Uploaded files must contain the following column which must be labeled in the first row of the file_\n
    `Review`, `Product_Name`
    """)
    fp = st.file_uploader('Upload JSON')
    
    if fp is not None:
        
       with st.spinner('Processing...'):
            st.success('File uploaded Successfully!')

   


    

    selection = st.selectbox("Select a model to process data:",("CD and Vinyl", "Digital Music","Pet Supplies","Industrial and Scientific","Arts and Craft"))
    
    if selection =="CD and Vinyl":
        lr_model = LogisticRegressionModel.load('models/model1.dat')
    if selection =="Digital Music":
        lr_model = LogisticRegressionModel.load('models/model1.dat')
    if selection =="Pet Supplies":
        lr_model = LogisticRegressionModel.load('models/model1.dat')
    if selection =="Industrial and Scientific":
        lr_model = LogisticRegressionModel.load('models/model1.dat')
    if selection =="Arts and Craft":
        lr_model = LogisticRegressionModel.load('models/model1.dat')
    
    if st.button("Start Analysis"):
        with st.spinner('Processing...'):
            # call model functions here
            main(fp, lr_model, spark)
            time.sleep(100)
            # st.header("Top Reviewed Products")
            # c1, c2, c3 = st.beta_columns((1, 1, 2))
            # c1.subheader("**Product**")
            # c2.subheader("**Overall Sentiment Score**")
            # c3.subheader("**Meaningful Words**")
            # for x in range(6):
            #     c1.write('Product #')
            #     c1, c2, c3 = st.beta_columns((1, 1, 2))
    
        