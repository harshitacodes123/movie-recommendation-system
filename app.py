import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('movie Recommendation System ')
option = st.selectbox(
    'how would you like to watch ?',
    (movies['title'].values)
)
if st.button('Recommend'):
    recommendations= recommend(option)
    for i in recommendations:
        st.write(i)