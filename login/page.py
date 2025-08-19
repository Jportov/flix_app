import streamlit as st
from login.service import login

def show_login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
        else:
            st.error("Login failed. Please try again.")
