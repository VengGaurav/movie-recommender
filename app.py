from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
from tmdb import fetch_movie_info
from generate_similarity import generate_similarity

app = Flask(__name__)

# Generate similarity.npy if it doesn't exist
if not os.path.exists("similarity.npy"):
    print("similarity.npy not found, generating...")
    generate_similarity()

# Load your movie data
movies = pd.read_csv("movies.csv")  # Make sure this file is pushed
similarity = np.load("similarity.npy", allow_pickle=True)

# Create a dictionary to map movie titles to indices
movie_indices = pd.Series(movies.index, index=movies['title']).to_dict()


def recommend(title):
    if title not in movie_indices:
        return []
    idx = movie_indices[title]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices_list = [i[0] for i in sim_scores]
    recommended = []

    for i in movie_indices_list:
        movie_title = movies.iloc[i]['title']
        info = fetch_movie_info(movie_title)
        recommended.append(info)

    return recommended


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        results = recommend(title)
        return render_template("index.html", results=results, query=title)
    else:
        # Default movies shown on homepage
        default_titles = ["Inception", "Interstellar", "The Dark Knight", "Avatar", "Avengers: Endgame"]
        results = [fetch_movie_info(t) for t in default_titles]
        return render_template("index.html", results=results, query=None)


if __name__ == "__main__":
    app.run(debug=True)
