import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


reviews = [
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

def show_reviews():
    st.subheader('Reviews Page')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )

    st.write('Create a new review.')
    name = st.text_input('Review Name')
    if st.button('Add Review'):
        st.success(f'Review \'{name}\' added successfully!')
