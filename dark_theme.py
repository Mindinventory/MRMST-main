import streamlit as st

# Set page config to wide mode
st.set_page_config(page_title="Dark Theme Streamlit", layout="wide")

# Define your dark theme using HTML and CSS
dark_theme = """
<style>
body {
    background-color: #121212; /* Background color */
    color: #FFFFFF; /* Text color */
}

/* Streamlit header */
.stApp h1 {
    color: #61dafb; /* Streamlit header color */
}

/* Streamlit sidebar */
.stSidebar {
    background-color: #1E1E1E; /* Sidebar background color */
    color: #FFFFFF; /* Sidebar text color */
}

/* Streamlit main content */
.stTextArea {
    background
