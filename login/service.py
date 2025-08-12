import streamlit as st 
from api.service import Auth

def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(username, password)
    
    if response.get('error'):
        st.error(f'Failed to login: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()