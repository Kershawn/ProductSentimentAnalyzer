import streamlit as st
import time

def app():
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


        