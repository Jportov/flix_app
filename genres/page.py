import pandas as pd
import streamlit as st
from genres.service import GenreService
from st_aggrid import AgGrid

def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros:')

        # Normaliza a lista de dicionários em DataFrame
        genres_df = pd.json_normalize(genres)

        # Garantir que tudo seja JSON serializável
        for col in genres_df.columns:
            genres_df[col] = genres_df[col].apply(
                lambda x: x if isinstance(x, (int, float, str, bool, type(None))) else str(x)
            )

        # Exibe a tabela no AgGrid
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        if not name.strip():
            st.error("O nome do gênero não pode estar vazio.")
            return

        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.success("Gênero cadastrado com sucesso!")
            st.experimental_rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')
