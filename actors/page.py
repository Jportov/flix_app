import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
import pandas as pd
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actor = actor_service.get_actors()
    
    if actor:
        st.subheader('Actors Page')
        actor_df = pd.json_normalize(actor)
        AgGrid(
            data=actor_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('No actors found.')
        
    st.write('Create a new actor.')
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=120, step=1)
    bio = st.text_area('Bio')
    date_of_birth = st.date_input(
        label='Date of Birth',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['American', 'British', 'Canadian', 'Australian', 'Indian', 'Other']
    nationality = st.selectbox('Nationality', nationality_dropdown)
    if st.button('Add'):
        new_actor = actor_service.create_actor(name=name, age=age, bio=bio, date_of_birth=date_of_birth, nationality=nationality)
        if new_actor:
            st.success('Actor created successfully!')
            st.rerun()
        else:
            st.error('Failed to create actor. Please try again.')
