import streamlit as st

st.title('My Chatbot')

upload_file = st.file_uploader("Upload")
if upload_file is not None:
    st.image(upload_file)
    