import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

img = Image.open('movie_recommendation.jpg')
st.set_page_config(page_title='Movie Recommender System', page_icon= img, layout= "wide")

def fetch_poster(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=31dee03c3f78740f33f912f067049607&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

similarity = pickle.load(open('similarity.pkl' , 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []
    for j in movies_list:
        movie_id = movies.iloc[j[0]].id
        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'What movie do you want to watch?',
    movies['title'].values
)



if st.button('Recommend'):
    names,posters  = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])



