import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


genres = [
    { 
        'id' : 1,
        'name': 'Action'
    },
    { 
        'id' : 2,
        'name': 'Comedy'
    },
    { 
        'id' : 3,
        'name': 'Drama'
    },
    { 
        'id' : 4,
        'name': 'Horror'
    },
    { 
        'id' : 5,
        'name': 'Sci-Fi'
    },
]

def show_genres():
    st.subheader('Genres Page')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
    )

    st.write('Create a new genre.')
    name = st.text_input('Genre Name')
    if st.button('Add Genre'):
        st.success(f'Genre \'{name}\' added successfully!')
