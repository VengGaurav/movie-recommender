from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
from tmdb import fetch_movie_info

app = Flask(__name__)

# Load data
movies = pd.read_csv("movies.csv")
similarity = np.load("similarity.npy", allow_pickle=True)

# Mapping movie titles to their indices
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
        default_titles = ["Inception", "Interstellar", "The Dark Knight", "Avatar", "Avengers: Endgame"]
        results = [fetch_movie_info(title) for title in default_titles]
        return render_template("index.html", results=results, query=None)


# Use this when deploying on Render (for dynamic port support)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
