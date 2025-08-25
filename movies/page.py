from datetime import datetime
import pandas as pd
import streamlit as st
from genres.service import GenreService
from actors.service import ActorService
from movies.service import MovieService
from st_aggrid import AgGrid, GridOptionsBuilder


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
    st.title('Filmes')

    # --- Formulário de cadastro ---
    st.subheader('Cadastrar Novo Filme')
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
    if st.button('Cadastrar', key='btn_add_movie'):
        if title.strip() == "":
            st.error("O título não pode ficar vazio!")
        else:
            new_movie = movie_service.create_movie(
                title=title,
                release_date=release_date,
                genre=genre_names[selected_genre_name],
                actors=selected_actors_ids,
                resume=resume,
            )
            if new_movie:
                st.session_state.movies = movie_service.get_movies()
                st.rerun()
            else:
                st.error('Erro ao cadastrar o filme. Verifique os campos')

    # --- Lista de filmes ---
    if 'movies' not in st.session_state:
        st.session_state.movies = movie_service.get_movies()
    movies = st.session_state.movies

    if movies:
        st.write('Lista de Filmes:')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        movies_df = clean_for_aggrid(movies_df)

        gb = GridOptionsBuilder.from_dataframe(movies_df)
        gb.configure_default_column(editable=False, sortable=True, filter=True, resizable=True)
        gb.configure_selection('single')
        gridOptions = gb.build()

        grid_response = AgGrid(
            movies_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            key='movies_grid',
        )

        selected = grid_response.get('selected_rows', [])
        if selected:
            selected_movie = selected[0]
            st.subheader(f"Editar Filme: {selected_movie['title']}")
            new_title = st.text_input('Novo título', value=selected_movie['title'], key='edit_movie_title')
            # Adicione campos para editar outros atributos se desejar
            if st.button('Salvar edição', key='btn_edit_movie'):
                # Implemente aqui a chamada para editar o filme via service/repository se disponível
                st.session_state.movies = movie_service.get_movies()
                st.rerun()
    else:
        st.warning('Nenhum filme encontrado.')