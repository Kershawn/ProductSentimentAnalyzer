import streamlit as st

def app(spark):
    st.title('File Upload')
    #  st.write('Welcome to the File Upload Page')

    st.write(
"""_Uploaded files must contain the following column which must be labeled in the first row of the file_\n
`Review`
""")
    fp = st.file_uploader('Upload CSV')