import streamlit as st
import main2
st.title("Bhavya's Movie Recommendation")
user_movie = st.selectbox("Choose a Movie",main2.df["title"])
if st.button("Recommend"):
    movies = main2.recommend(str(user_movie))
    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.image(movies[idx]["poster"], use_container_width=True)
            st.markdown(f"<center><b>{movies[idx]['title']}</b></center>", unsafe_allow_html=True)