import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
spark = SparkSession.builder.master('local[*]').appName('Big Data Project').getOrCreate()
sc = spark.sparkContext

import streamlit as st

import pages.productanalysis as pa
import pages.home as home


st.set_page_config(layout="wide")
st.sidebar.title('Navigation')

PAGES = {
    "Home": home,
    "Product Analysis": pa,
}

selection = st.sidebar.radio('Go to ', list(PAGES.keys()))

page = PAGES[selection]
page.app(spark)
