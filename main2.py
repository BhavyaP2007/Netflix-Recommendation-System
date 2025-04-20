import pandas as pd
import pathlib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
cv = CountVectorizer(max_features=2500, stop_words="english")
root = pathlib.Path(__file__).parent
df = pd.read_csv(str(root).replace("\\","/")+"/dataset2.csv")
df["tags"] = df["tags"] + " " + df["title"]
pd.set_option("display.max_columns",None)
vectors = cv.fit_transform(df["tags"])
vectors_dense = vectors.toarray()
def recommend(movie):
    similar_movies = []
    index_of_movie = df.loc[df["title"].str.lower() == movie.lower()].index.to_list()[0]
    similarity = cosine_similarity(vectors[index_of_movie],vectors).flatten()
    indexed_similarity = list(enumerate(similarity))
    indexed_similarity = sorted(indexed_similarity,key= lambda x: x[1],reverse=True)
    for i in indexed_similarity[1:6]:
        movie_data = df.loc[i[0],["title","poster_path"]].to_list()
        similar_movies.append({"title":movie_data[0],"poster":"https://image.tmdb.org/t/p/w500"+movie_data[1]})
    return similar_movies   
recommend("Doctor Strange")     