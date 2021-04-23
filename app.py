import streamlit as st
import pages.productanalysis as pa
import pages.home as home

# st.title('Home')
# st.write('Welcome to the homepage')
st.set_page_config(layout="wide")
st.sidebar.title('Navigation')

PAGES = {
    "Home": home,
    "Product Analysis": pa,
}

# Add a radio button to the sidebar:
selection = st.sidebar.radio(
    'Go to ',
    list(PAGES.keys())
)

page = PAGES[selection]
page.app()