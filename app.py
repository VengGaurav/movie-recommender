import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from generate_similarity import generate_similarity
from tmdb import fetch_movie_info

app = Flask(__name__)

# Auto-generate similarity.npy if not present
if not os.path.exists("similarity.npy"):
    print("similarity.npy not found. Generating now...")
    generate_similarity()

# Then load it
similarity = np.load("similarity.npy", allow_pickle=True)
movies = pd.read_csv("movies.csv")


# Create a dictionary to map movie titles to indices
movie_indices = pd.Series(movies.index, index=movies['title']).to_dict()


def recommend(title):
    # First, try to find the movie with fuzzy matching
    title_lower = title.lower()
    matching_movies = []
    
    # Search for movies containing the search term
    for movie_title in movies['title']:
        if title_lower in movie_title.lower():
            matching_movies.append(movie_title)
    
    if not matching_movies:
        return []
    
    # Use the first matching movie for recommendations
    selected_movie = matching_movies[0]
    
    if selected_movie not in movie_indices:
        return []
    
    idx = movie_indices[selected_movie]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices_list = [i[0] for i in sim_scores]
    recommended = []

    # Use local data instead of API calls for faster results
    for i in movie_indices_list:
        movie_data = movies.iloc[i]
        info = {
            'title': movie_data['title'],
            'overview': movie_data['overview'] if pd.notna(movie_data['overview']) else "No overview available.",
            'poster': None  # We'll skip poster for now to improve speed
        }
        recommended.append(info)

    return recommended




@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        results = recommend(title)
        
        # Find which movie was actually used for recommendations
        title_lower = title.lower()
        matching_movies = []
        for movie_title in movies['title']:
            if title_lower in movie_title.lower():
                matching_movies.append(movie_title)
        
        selected_movie = matching_movies[0] if matching_movies else title
        
        return render_template("index.html", results=results, query=title, selected_movie=selected_movie, matching_movies=matching_movies)
    else:
        # Default movies shown on homepage - use local data for speed
        default_indices = [0, 1, 2, 3, 4]  # First 5 movies as examples
        results = []
        for idx in default_indices:
            movie_data = movies.iloc[idx]
            info = {
                'title': movie_data['title'],
                'overview': movie_data['overview'] if pd.notna(movie_data['overview']) else "No overview available.",
                'poster': None
            }
            results.append(info)
        return render_template("index.html", results=results, query=None, selected_movie=None, matching_movies=None)


if __name__ == "__main__":
    app.run(debug=True)
