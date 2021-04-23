import streamlit as st
import pages.productanalysis as pa
import pages.negativeproducts as np
import pages.fileupload as fu
import pages.home as home

# st.title('Home')
# st.write('Welcome to the homepage')
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
page.app()