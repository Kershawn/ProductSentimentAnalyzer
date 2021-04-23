import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
spark = SparkSession.builder.master('local[*]').appName('Big Data Project').getOrCreate()
sc = spark.sparkContext

import streamlit as st

import pages.productanalysis as pa
import pages.negativeproducts as np
import pages.fileupload as fu
import pages.home as home

# st.title('Home')
# st.write('Welcome to the homepage')
st.set_page_config(layout="wide")
st.sidebar.title('Navigation')

PAGES = {
    "Home": home,
    "File Upload": fu,
    "Product Analysis": pa,
    "Negative Products": np
}

# Add a radio button to the sidebar:
selection = st.sidebar.radio(
    'Go to ',
    list(PAGES.keys())
)

page = PAGES[selection]
page.app(spark)