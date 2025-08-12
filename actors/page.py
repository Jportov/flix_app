import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


actors = [
    { 
        'id' : 1,
        'name': 'Robert Downey Jr.'
    },
    { 
        'id' : 2,
        'name': 'Chris Evans'
    },
    { 
        'id' : 3,
        'name': 'Scarlett Johansson'
    },
    { 
        'id' : 4,
        'name': 'Chris Hemsworth'
    },
    { 
        'id' : 5,
        'name': 'Tom Hiddleston'
    },
]

def show_actors():
    st.subheader('Actors Page')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid'
    )

    st.write('Create a new actor.')
    name = st.text_input('Actor Name')
    if st.button('Add Actor'):
        st.success(f'Actor \'{name}\' added successfully!')
