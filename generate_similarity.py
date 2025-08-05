import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_similarity():
    # Load the dataset
    movies = pd.read_csv("movies.csv")

    # Fill any missing overviews with empty string
    movies['overview'] = movies['overview'].fillna('')

    # Create TF-IDF vectorizer and transform the overview column
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)  # Limit features for speed
    tfidf_matrix = tfidf.fit_transform(movies['overview'])

    # Compute cosine similarity matrix
    similarity = cosine_similarity(tfidf_matrix)

    # Save the similarity matrix to a .npy file
    np.save("similarity.npy", similarity)
    print("similarity.npy file generated successfully.")

# Run the function if script is executed
if __name__ == "__main__":
    generate_similarity()
