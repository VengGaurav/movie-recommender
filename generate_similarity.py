import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your dataset
movies = pd.read_csv('movies.csv')

# Combine important features into a single string
def combine_features(row):
    return str(row['title']) + " " + str(row['genres']) + " " + str(row['overview'])

movies['combined'] = movies.apply(combine_features, axis=1)

# Vectorize the combined features
cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(movies['combined'])

# Compute cosine similarity
similarity = cosine_similarity(count_matrix)

# Save to file
np.save('similarity.npy', similarity)

print("✅ similarity.npy generated successfully!")
