import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
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


def show_reviews():
    review_service = ReviewService()
    st.title('Avaliações')

    # --- Lista de avaliações ---
    if 'reviews' not in st.session_state:
        st.session_state.reviews = review_service.get_reviews()
    reviews = st.session_state.reviews

    if reviews:
        st.write('Lista de Avaliações:')
        reviews_df = pd.json_normalize(reviews)
        reviews_df = clean_for_aggrid(reviews_df)

        gb = GridOptionsBuilder.from_dataframe(reviews_df)
        gb.configure_default_column(editable=False, sortable=True, filter=True, resizable=True)
        gb.configure_selection('single')
        gridOptions = gb.build()

        grid_response = AgGrid(
            reviews_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            key='reviews_grid',
        )

        selected = grid_response.get('selected_rows', [])
        if selected:
            selected_review = selected[0]
            st.subheader(f"Editar Avaliação do Filme: {selected_review['movie']}")
            new_comment = st.text_area('Novo comentário', value=selected_review['comment'], key='edit_review_comment')
            # Adicione campos para editar estrelas ou filme se desejar
            if st.button('Salvar edição', key='btn_edit_review'):
                # Implemente aqui a chamada para editar a avaliação via service/repository se disponível
                st.success("Avaliação atualizada!")
                st.session_state.reviews = review_service.get_reviews()
                st.experimental_rerun()
    else:
        st.warning('Nenhuma avaliação encontrada.')

    # --- Formulário de cadastro ---
    st.subheader('Cadastrar Nova avaliação')
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))
    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )
    comment = st.text_area(label='Comentário')
    if st.button('Cadastrar Nova', key='btn_add_review'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.success("Avaliação cadastrada com sucesso!")
            st.session_state.reviews = review_service.get_reviews()
            st.experimental_rerun()
        else:
            st.error('Erro ao cadastrar a avaliação. Verifique os campos')