import pandas as pd
import streamlit as st
from genres.service import GenreService
from st_aggrid import AgGrid, ExcelExportMode


def clean_for_aggrid(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte tudo que não for string, número ou boolean em string,
    para evitar problemas de serialização no AgGrid.
    """
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col]):
            df[col] = df[col].apply(lambda x: str(x) if not pd.isnull(x) else '')
    return df


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros:')
        genres_df = pd.json_normalize(genres)
        genres_df = clean_for_aggrid(genres_df)  # limpa antes de passar pro AgGrid
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(
            name=name,
        )
        if new_genre:
            st.experimental_rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')