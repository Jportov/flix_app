import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


movies = [
    { 
        'id' : 1,
        'name': 'Purge'
    },
    { 
        'id' : 2,
        'name': 'The Conjuring'
    },
    { 
        'id' : 3,
        'name': 'Inception'
    },
    { 
        'id' : 4,
        'name': 'Avatar'
    },
    { 
        'id' : 5,
        'name': 'Interstellar'
    },
]

def show_movies():
    st.subheader('Movies Page')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )

    st.write('Create a new movie.')
    name = st.text_input('Movie Name')
    if st.button('Add Movie'):
        st.success(f'Movie \'{name}\' added successfully!')
