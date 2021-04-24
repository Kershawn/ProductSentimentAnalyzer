import streamlit as st
import time
import pandas as pd

import findspark
 #findspark.find()
findspark.init()
from pyspark.ml.classification import LogisticRegressionModel

from pages.fileupload2 import main


def app(spark):
    st.title('Product Analysis')
    st.write('Welcome to Product Analysis')

    st.write(
    """_Uploaded files must contain the following column which must be labeled in the first row of the file_\n
    `Review`, `Product_Name`
    """)
    
    selection = st.selectbox("Select a model to process data:",("CD and Vinyl", "Digital Music","Pet Supplies","Industrial and Scientific","Arts and Craft"))
    fp = st.file_uploader('Upload JSON or CSV')
    
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

    if fp is not None:
        main(fp, lr_model, spark)
        