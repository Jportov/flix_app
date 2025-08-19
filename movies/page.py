import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from movies.service import MovieService
from datetime import datetime
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()
    
    if movies:
        st.subheader('Movies Page')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre_id'], errors='ignore')
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid'
        )
    else:
        st.warning("No movies found. Please check your connection or try again later.")

    st.write('Create a new movie.')
    title = st.text_input('Title')
    description = st.text_area('Description')
    release_date = st.date_input(
        label='Release Date',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD-MM-YYYY'
    )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_name = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Genre', list(genre_name.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Select Actors', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]
    description = st.text_area('Resume', height=100)

    if st.button('Add Movie'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_name[selected_genre_name],
            actors=selected_actors_ids,
            description=description
        )
        if new_movie:
            st.rerun()
            st.success(f'Movie \'{title}\' added successfully!')
        else:
            st.error('Failed to add movie. Please try again.')
