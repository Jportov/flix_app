import streamlit as st
import requests
from login.service import logout


class MovieRepository: 
    
    def __init__(self):
        self.__base_url = 'https://portodevs.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url, 
            headers=self.__headers
            )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
        raise Exception(f'Failed to obtain API data. Status code: {response.status_code}, Response: {response.text}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 400:
            st.error('Movie already exists. Please check your input.')
            return None
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
        raise Exception(f'Failed to create Movie. Status code: {response.status_code}, Response: {response.text}')

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
        raise Exception(f'Failed to obtain movie stats. Status code: {response.status_code}, Response: {response.text}')