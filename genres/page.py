import pandas as pd
import streamlit as st
from genres.service import GenreService
from st_aggrid import AgGrid, GridOptionsBuilder

def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    st.title('Gêneros')

    if genres:
        st.write('Lista de Gêneros:')
        genres_df = pd.json_normalize(genres)

        # Cria GridOptions
        gb = GridOptionsBuilder.from_dataframe(genres_df)
        gb.configure_default_column(
            editable=False, 
            sortable=True, 
            filter=True, 
            resizable=True
        )
        gridOptions = gb.build()

        AgGrid(
            genres_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            key='genres_grid'
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.subheader('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.experimental_rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')
