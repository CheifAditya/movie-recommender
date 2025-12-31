import pandas as pd
import numpy as np


#Loading CSV
movies_df = pd.read_csv(r"C:\Users\Aditya Singh\AI ML\PROJECT WORK\Dataset\tmdb_5000_movies.csv")

#Data Cleaning because API will load data from original CSV
movies_df["overview"] = movies_df["overview"].fillna('')


#Loading tfidf data and tfidf_matrix

import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

with open(os.path.join(MODEL_DIR, "vectorizer.pkl"), "rb") as f:
    tfidf = pickle.load(f)

with open(os.path.join(MODEL_DIR, "tfidf_matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)

#recommend function
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_name,top_n = 5):

    #Case insensitive search and partial matching
    movie_name = movie_name.lower()
    movie_series_lc = pd.Series(movies_df["title"].str.lower(),name="title")
    find_movie = movie_series_lc[movie_series_lc == movie_name].empty  
    if find_movie == False :
        movie_row = movie_series_lc[movie_series_lc == movie_name].index[0]        
    else :
        if (movie_series_lc.str.contains(movie_name)).any():                
            movie_row = movie_series_lc[movie_series_lc.str.contains(movie_name)].index[0]
        else:
            return None
    movie_vector = tfidf_matrix[movie_row]              
    
    similarity_scores = cosine_similarity(movie_vector,tfidf_matrix)    
    similarity_scores = similarity_scores[0]    

    top_indices_list = np.argsort(similarity_scores)[::-1]       
    top_indices_list = top_indices_list[1:top_n+1]

    similar_movies_list = []
    for idx in top_indices_list :
        movie = {"title":movies_df.loc[idx,"title"],"overview":movies_df.loc[idx,"overview"]}
        similar_movies_list.append(movie)

    return similar_movies_list