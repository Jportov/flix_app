import streamlit as st

# Page configuration
st.set_page_config(
    page_title="About - Flix App",
    page_icon="ℹ️",
    layout="wide"
)

def show_about():
    # Title
    st.title("ℹ️ About Flix App")

    # Description
    st.markdown("""
    **Flix App** was born out of a passion for movies and technology.

    🎯 **Our mission** is to deliver a complete experience for movie lovers, allowing them to discover, explore, and share their favorite films in a simple and intuitive way.

    **Current features include:**
    - Searchable movie catalog
    - Movie details including summaries, ratings, and trailers
    - Lightweight and responsive interface

    Stay tuned for upcoming features like personalized recommendations, collaborative lists, and streaming platform integration!

    ---
    """)

    # Team (example)
    st.header("👨‍💻 Our Team")
    st.markdown("""
    - **João Silva** — Backend Developer  
    - **Maria Oliveira** — UI/UX Designer  
    - **Carlos Lima** — Data Specialist
    """)

    # Contact
    st.markdown("---")
    st.header("📫 Contact Us")
    st.markdown("""
    Feel free to reach out with questions, suggestions, or partnership opportunities:

    - Email: `contact@flixapp.com`  
    - GitHub: [github.com/flixapp](https://github.com/)  
    - Instagram: [@flixappofficial](https://instagram.com/)
    """)

    st.markdown("---")
    st.caption("© 2025 Flix App — All rights reserved.")

# Run if this script is executed directly
if __name__ == "__main__":
    show_about()
