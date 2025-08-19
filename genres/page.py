import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService



def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()
    
    if genres:
        st.subheader('Genres Page')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid'
        )
    else:
        st.warning('No genres available.')
        
    st.write('Create a new genre.')
    name = st.text_input('Genre Name')
    if st.button('Add Genre'):
        new_genre = genre_service.create_genre(
            name=name,
            )
        if new_genre:
            st.success(f'Genre \'{name}\' added successfully!')
            st.rerun()
        else:
            st.error('Failed to add genre. Please try again.')
