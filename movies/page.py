from datetime import datetime
import pandas as pd
import streamlit as st
from genres.service import GenreService
from actors.service import ActorService
from movies.service import MovieService
from st_aggrid import AgGrid


def clean_for_aggrid(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte tudo que não for string, número ou boolean em string,
    para evitar problemas de serialização no AgGrid.
    """
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col]):
            df[col] = df[col].apply(lambda x: str(x) if not pd.isnull(x) else '')
    return df


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes:')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        movies_df = clean_for_aggrid(movies_df)

        AgGrid(
            data=movies_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar Novo Filme')

    title = st.text_input('Título')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.experimental_rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')