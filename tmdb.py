import requests

API_KEY = 'ba05d12a23dd093e0bab3023293264a4'  # 🔁 Replace this with your API key
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def fetch_movie_info(title):
    params = {
        'api_key': API_KEY,
        'query': title
    }
    response = requests.get(TMDB_SEARCH_URL, params=params)
    data = response.json()

    if data['results']:
        movie = data['results'][0]
        return {
            'title': movie.get('title'),
            'overview': movie.get('overview'),
            'poster': TMDB_IMAGE_BASE + movie['poster_path'] if movie.get('poster_path') else None
        }
    return {
        'title': title,
        'overview': "Overview not found.",
        'poster': None
    }
