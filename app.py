import streamlit as st
import pickle
import nltk
# import sklearn
import pandas as pd
import joblib

st.title("Movie Recommendation System")

with open("movies.pickle","rb") as f:
    movies = pickle.load(f)

similarities = joblib.load("similarity.joblib")
movie_names=movies['title'].values

def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    distances=similarities[movie_index]
    movie_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

name_movie=st.selectbox("Select a movie",movie_names)

if st.button("Recommend"):
    r=recommend(name_movie)
    
    st.write("The Recommended Movies are:")
    for i in r:
        st.write(i)