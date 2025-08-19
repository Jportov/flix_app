import requests
import streamlit as st 
from login.service import logout


class ActorRepository:
    
    def __init__(self):
        self.__base_url = 'https://portodevs.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
        raise Exception(f'Failed to obtain API data. Status code: {response.status_code}, Response: {response.text}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            st.error("Unauthorized access. Please log in again.")
            st.session_state.pop('token', None)
        raise Exception(f'Failed to create actor. Status code: {response.status_code}, Response: {response.text}')
