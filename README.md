# 🎬 Movie Recommendation System

A smart movie recommendation web application built with Flask that uses machine learning to suggest similar movies based on content-based filtering. The system analyzes movie overviews, genres, and keywords to find the most similar films.

## ✨ Features

- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity to find similar movies
- **Smart Search**: Fuzzy matching and partial search capabilities for movie titles
- **Real Movie Posters**: Integrates with TMDB API to fetch actual movie posters
- **Modern UI**: Clean, responsive design with dark/light theme toggle
- **Popular Movies**: Shows trending movies on the homepage
- **Detailed Information**: Displays movie titles, overviews, and posters for recommendations

## 🚀 Live Demo

[Add your deployed application URL here]

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: TMDB (The Movie Database) API
- **Deployment**: Heroku (with Procfile and runtime.txt)

## 📋 Prerequisites

- Python 3.8 or higher
- TMDB API key (free at [themoviedb.org](https://www.themoviedb.org/settings/api))

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/recommender-app.git
   cd recommender-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your TMDB API key**
   
   Edit `tmdb.py` and replace the API key:
   ```python
   API_KEY = 'your_tmdb_api_key_here'
   ```

5. **Prepare the dataset**
   
   Make sure you have a `movies.csv` file in the root directory with the following columns:
   - `title`: Movie title
   - `overview`: Movie description
   - `genres`: Movie genres (comma-separated)
   - `keywords`: Movie keywords (comma-separated)

6. **Generate similarity matrix**
   ```bash
   python generate_similarity.py
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Search for movies**
   - Enter a movie title in the search box
   - Click "Recommend" to get similar movie suggestions
   - Browse popular movies on the homepage

## 📁 Project Structure

```
recommender-app/
├── app.py                 # Main Flask application
├── generate_similarity.py # ML model for generating similarity matrix
├── tmdb.py               # TMDB API integration
├── movies.csv            # Movie dataset (not included in repo)
├── similarity.npy        # Pre-computed similarity matrix
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python runtime specification
├── static/
│   └── style.css        # CSS styles
└── templates/
    └── index.html       # Main HTML template
```

## 🤖 How It Works

1. **Data Processing**: The system loads movie data from `movies.csv` and combines overview, genres, and keywords into a single feature vector.

2. **Feature Extraction**: Uses TF-IDF vectorization to convert text features into numerical vectors, capturing the importance of words in the context of the entire dataset.

3. **Similarity Calculation**: Computes cosine similarity between all movie pairs to create a similarity matrix.

4. **Recommendation Engine**: When a user searches for a movie, the system:
   - Finds the closest matching movie using fuzzy search
   - Retrieves the similarity scores for that movie
   - Returns the top 5 most similar movies

5. **Enhanced Display**: Fetches real movie posters and information from TMDB API for a better user experience.

## 🚀 Deployment

### Deploy to Heroku

1. **Create a Heroku account** and install the Heroku CLI

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set TMDB_API_KEY=your_api_key_here
   ```

5. **Deploy the application**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

6. **Open the deployed app**
   ```bash
   heroku open
   ```

## 📊 Dataset

The application requires a `movies.csv` file with the following structure:

```csv
title,overview,genres,keywords
"Avatar","A paraplegic marine dispatched to the moon Pandora...","Action,Adventure,Fantasy","culture clash,future,space war..."
"The Dark Knight","When the menace known as the Joker...","Action,Crime,Drama","dc comics,crime fighter,terrorist..."
```

## 🔧 Configuration

### Environment Variables

- `TMDB_API_KEY`: Your TMDB API key for fetching movie posters

### Customization

- Modify `generate_similarity.py` to adjust the ML model parameters
- Update the popular movies list in `app.py` for different homepage content
- Customize the UI by editing `static/style.css`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing movie data and posters
- [scikit-learn](https://scikit-learn.org/) for machine learning capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or contact [your-email@example.com].

---

⭐ **Star this repository if you found it helpful!**
