import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies = pickle.load(open('movies_name.pkl', 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity_array.pkl','rb'))


st.title('Movie Recommender System')

option = st.selectbox('How would you like to be contacted?',
                      movies_list)

if st.button('Recommend'):
    recommended_movies, recommended_movies_poster = recommend(option)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_poster[4])
    with col6:
        st.text(recommended_movies[5])
        st.image(recommended_movies_poster[5])
    with col7:
        st.text(recommended_movies[6])
        st.image(recommended_movies_poster[6])
