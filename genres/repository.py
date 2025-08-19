import streamlit as st
import requests
from login.service import logout


class GenreRepository: 
    
    def __init__(self):
        self.__base_url = 'https://portodevs.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url, 
            headers=self.__headers
            )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
            st.session_state.pop('token', None)
        raise Exception(f'Failed to obtain API data. Status code: {response.status_code}, Response: {response.text}')

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 400:
            st.error('Genre already exists. Please check your input.')
            return None
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
            st.session_state.pop('token', None)
        raise Exception(f'Failed to create genre. Status code: {response.status_code}, Response: {response.text}')
