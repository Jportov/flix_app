import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Flix App",
    page_icon="🎬",
    layout="wide"
)

def show_home():
    # Header
    st.title("🎬 Flix App")
    st.subheader("Welcome to your ultimate movie hub!")

    # Description
    st.markdown("""
    **Flix App** is your ultimate destination to discover, explore, and fall in love with movies.
    
    Here, you can:
    - 🔍 Search for your favorite movies
    - 🌟 View ratings and summaries
    - 📺 Watch trailers
    - 💾 Save movies to watch later

    Enjoy the cinema experience at home! 🍿
    """)

    # Banner image
    st.image("https://images.unsplash.com/photo-1581905764498-31c6d14bfac7?fit=crop&w=1200&q=80", use_container_width=True)

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
