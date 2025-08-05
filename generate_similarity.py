import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_similarity():
    # Load the dataset
    movies = pd.read_csv("movies.csv")

    # Fill any missing overviews with empty string
    movies['overview'] = movies['overview'].fillna('')
    movies['genres'] = movies['genres'].fillna('[]')
    movies['keywords'] = movies['keywords'].fillna('[]')

    # Extract genres and keywords
    def extract_features(text):
        if text == '[]':
            return ''
        # Remove quotes and brackets, split by comma
        text = text.replace('"', '').replace('[', '').replace(']', '')
        features = [item.strip() for item in text.split(',') if item.strip()]
        return ' '.join(features)

    # Create combined features
    movies['combined_features'] = (
        movies['overview'] + ' ' + 
        movies['genres'].apply(extract_features) + ' ' + 
        movies['keywords'].apply(extract_features)
    )

    # Create TF-IDF vectorizer with better parameters
    tfidf = TfidfVectorizer(
        stop_words='english', 
        max_features=10000,
        ngram_range=(1, 2),  # Use both single words and word pairs
        min_df=2,  # Minimum document frequency
        max_df=0.8  # Maximum document frequency
    )
    
    tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

    # Compute cosine similarity matrix
    similarity = cosine_similarity(tfidf_matrix)

    # Save the similarity matrix to a .npy file
    np.save("similarity.npy", similarity)
    print("similarity.npy file generated successfully with improved features.")

# Run the function if script is executed
if __name__ == "__main__":
    generate_similarity()
