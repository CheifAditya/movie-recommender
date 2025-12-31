## Project Title: Movie Recommendation System using TF-IDF & Cosine Similarity


## Project Overview:

This project implements a content-based movie recommendation system that suggests similar movies using TF-IDF vectorization and cosine similarity.The system performs a lexical similarity search based on movie metadata such as title, genres, overview, and keywords, and returns the top 5 most similar movies for a given input movie.The project focuses on explainability and simplicity, making it suitable for understanding the fundamentals of content-based recommendation systems.

## Key Features

- Content-based movie recommendation system
- Uses **TF-IDF vectorization** to convert movie metadata into numerical feature vectors
- Applies **cosine similarity** to perform lexical similarity search between movies
- Implements **pickling** to persist trained models and reduce recomputation
- Implements **case-insensitive** and **partial movie name** search
- Handles **movie-not-found** edge cases gracefully
- Provides a **clean and readable output**, displaying the top-N recommended movies along with their short overviews


## How the System Works

1. Movie metadata such as title, genres, overview, and keywords are preprocessed and combined into a single textual representation.
2. The combined text is cleaned and missing values are handled to ensure consistency.
3. TF-IDF vectorization is applied to convert movie text into numerical feature vectors.
4. Cosine similarity is computed between the selected movie and all other movies to measure lexical similarity.
5. Movies are ranked based on similarity scores.
6. The top-N most similar movies (default N = 5) are returned as recommendations.


## Technologies Used

- Programming Language: Python,HTML,CSS
- Libraries: Numpy, Pandas, Scikit-learn, FastAPI
- Tools: Jupyter Notebook


## Project Structure

- notebooks         # EDA and experimentation
- src               # core recommender logic
- README.md         # Project Details

## Limitations 

- TF-IDF works on the basis of lexical similarity not semantic similarity
- TF-IDF doesnt understands literal meaning of words, their synonyms,etc.
- Recommendations depend on just textual overlap 

## How to Run this project locally
1. Clone the repository
``` bash
git clone https://github.com/CheifAditya/movie-recommender.git
cd movie-recommender
```

2. Install dependencies
``` bash
pip install -r requirements.txt
```

3. Run the Fast API application
``` bash
uvicorn src.api:app --reload
```

4. Open in browser the Web UI
``` bash
http://127.0.0.1:8000/
```


