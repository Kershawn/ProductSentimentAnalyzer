import streamlit as st
import time

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

   


    

    st.selectbox("Select a model to process data:",["CD and Vinyl", "Digital Music","Pet Supplies","Industrial and Scientific","Arts and Craft"] )

    st.header("Top Reviewed Products")
    c1, c2, c3 = st.beta_columns((1, 1, 2))
    c1.subheader("**Product**")
    c2.subheader("**Overall Sentiment Score**")
    c3.subheader("**Meaningful Words**")
    for x in range(6):
        c1.write('Product #')
        c1, c2, c3 = st.beta_columns((1, 1, 2))
    
        