import streamlit as st 
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home
from about.page import show_about
from login.page import show_login


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        
        menu_options = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Home', 'Genres', 'Movies', 'Reviews','Actors/Actress', 'About'])
        
        if menu_options == 'Home':
            show_home()
            
        if menu_options == 'Genres':
            show_genres()
            
        if menu_options == 'Movies':
            show_movies()

        if menu_options == 'Reviews':
            show_reviews()
            
        if menu_options == 'Actors/Actress':
            show_actors()
            
        if menu_options == 'About':
            show_about()


if __name__ == "__main__":
    main()