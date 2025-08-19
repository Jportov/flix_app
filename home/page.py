import streamlit as st
from movies.service import MovieService
import plotly.express as px

st.set_page_config(
    page_title="Flix App",
    page_icon="🎬",
    layout="wide"
)

def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()
    
    st.title("Movies stats")
    
    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader("Here's a quick overview of our movies by genre:")
        fig = px.pie(
            movie_stats['movies_by_genre'], 
            names='genre__name', 
            values='count', 
            title='Movies by Genre'
        )

        st.plotly_chart(fig)

        st.subheader("Here's a quick overview of our movie collection:")
        st.write(movie_stats['total_movies'])

        st.subheader("Here's a quick overview of our movies reviews collection:")
        st.write(movie_stats['total_reviews'])
        
        st.subheader("Here's a quick overview of our stars on reviews")
        st.write(movie_stats['total_stars'])


    # Upcoming features
    st.markdown("---")
    st.header("🚀 Coming Soon")
    st.markdown("""
    - Personalized recommendations based on your preferences
    - Collaborative movie lists with friends
    - Alerts for premieres and new releases
    """)

    # Footer
    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit · 2025")

# Run if this script is executed directly
if __name__ == "__main__":
    show_home()
