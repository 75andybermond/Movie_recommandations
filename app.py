from flask import Flask,render_template,request

import numpy as np
import pandas as pd
import pickle
import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
# Set the sqlite connector 
conn = sqlite3.connect('movies.db')

# Make a df with the strings and combine them to only one column 
r_df = pd.read_sql('SELECT directors,fullplot,casting,countries, genres, languages FROM movies;',con= conn)
r_df = r_df.applymap(lambda x: x.strip().replace("  "," "))    
combined_features = r_df['directors']+' '+r_df['fullplot']+' '+ r_df['casting']+' '+ r_df['countries']+' '+ r_df['genres'] + ' ' + r_df['languages'] 

# Use Tf-idf vectorization to convert the combined string into numerical feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Calculate the cosine similarity between all feature vectors
similarity = cosine_similarity(feature_vectors)

def recommend_movies(movie_name):
     """
     Connects to the 'movies.db' SQLite database and retrieves the 'id' and 'title' columns from the 'movies' table.
     Creates a pandas series with the index set to the 'title' column, and the corresponding index set to the 'id' column.
     Removes duplicates from the series by keeping the last occurence of each title.
     Check if the input movie name is present in the index of the series, if not it returns an empty list.
     Retrieves the index of the input movie name from the series.
     Retrieves the cosine similarity scores for the input movie from the precomputed similarity matrix.
     Creates a new dataframe with the similarity scores and selects the top 5 movies with the highest scores.
     Retrieves the title of the recommended movies from the original series dataframe using the selected indices.
     Returns:  the recommended movie titles as a list.
     """
     conn = sqlite3.connect('movies.db')
     series = pd.read_sql('SELECT id, title FROM movies;',con= conn)
     indices = pd.Series(series.index, index=series['title'])
     indices = indices[~indices.index.duplicated(keep='last')]
     if movie_name not in indices.index:
          return []
     idx = indices[movie_name]
     if idx is None:
          return []
     sim_scores = pd.DataFrame(similarity[idx], columns=["score"])
     sim_scores = sim_scores[0:10]
     movie_indices = sim_scores.sort_values("score", ascending=False)[0:5].index.tolist()
     recommended_movies = series.iloc[movie_indices]['title']

     return recommended_movies.tolist()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    '''
    Interact with the user's query and return recommended movies
    '''
    # Get the user's input from the form values
    features = [str(x) for x in request.form.values()]
    print(features)
    movie_name = str(features[0])
    print(movie_name)
    # Call the recommend_movies function to get the recommended movies
    output = recommend_movies(movie_name)
    print(f'output')
    # Render the result on the HTML template
    return render_template('index.html', recommended_movie=output)


if(__name__=='__main__'):
    app.run(debug=True)

# Run it :)fgvfg