import pandas as pd
import streamlit as st
from genres.service import GenreService
from st_aggrid import AgGrid, GridOptionsBuilder

def clean_for_aggrid(df: pd.DataFrame) -> pd.DataFrame:
    # Converte colunas não numéricas/booleanas para string
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col]):
            df[col] = df[col].apply(lambda x: str(x) if not pd.isnull(x) else '')
    return df

def show_genres():
    genre_service = GenreService()

    st.title('Gêneros')

    # --- Formulário de cadastro ---
    st.subheader('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        if name.strip() == "":
            st.error("O nome do gênero não pode ficar vazio!")
        else:
            new_genre = genre_service.create_genre(name=name)
            if new_genre:
                st.success(f"Gênero '{name}' cadastrado com sucesso!")
                st.experimental_rerun()  # força atualização da página
            else:
                st.error("Erro ao cadastrar o gênero. Verifique os campos.")

    # --- Lista de gêneros ---
    genres = genre_service.get_genres()
    if genres:
        st.write('Lista de Gêneros:')
        genres_df = pd.json_normalize(genres)
        genres_df = clean_for_aggrid(genres_df)

        # Configura AgGrid
        gb = GridOptionsBuilder.from_dataframe(genres_df)
        gb.configure_default_column(editable=False, sortable=True, filter=True, resizable=True)
        gb.configure_selection('single')
        gridOptions = gb.build()

        grid_response = AgGrid(
            genres_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            key='genres_grid'
        )

        # --- Edição de gênero ---
        selected = grid_response.get('selected_rows', [])
        if selected:
            selected_genre = selected[0]
            st.subheader(f"Editar Gênero: {selected_genre['name']}")
            new_name = st.text_input('Novo nome', value=selected_genre['name'], key='edit_genre_name')
            if st.button('Salvar edição'):
                # Implemente aqui a chamada para editar o gênero via service/repository se disponível
                # Exemplo: genre_service.edit_genre(selected_genre['id'], new_name)
                st.success(f"Gênero atualizado para '{new_name}'")
                st.experimental_rerun()
    else:
        st.warning('Nenhum gênero encontrado.')
