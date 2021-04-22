import streamlit as st
import positiveproducts, negativeproducts, fileupload, home

# st.title('Home')
# st.write('Welcome to the homepage')
st.sidebar.title('Navigation')

PAGES = {
    "Home": home,
    "File Upload": fileupload,
    "Positive Products": positiveproducts,
    "Negative Products": negativeproducts
}

# Add a radio button to the sidebar:
selection = st.sidebar.radio(
    'Go to ',
    list(PAGES.keys())
)

page = PAGES[selection]
page.app()