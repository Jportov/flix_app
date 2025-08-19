import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    
    if reviews:
        st.subheader('Reviews Page')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.write('No reviews available.')
        
    st.subheader('Add a Review')
    
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['title'] for movie in movies}
    selected_movie_title = st.selectbox('Movie', list(movie_titles.keys()))
    
    stars = st.number_input(
        label='Stars',
        min_value=1,
        max_value=5,
        step=1,
    )
    comment = st.text_area(
        label='Comment')
    if st.button('Add Review'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            comment=comment,
            stars=stars
        )
        if new_review:
            st.rerun()
            st.success(f'Review for \'{selected_movie_title}\' added successfully!')
        else:
            st.error('Failed to add review.')