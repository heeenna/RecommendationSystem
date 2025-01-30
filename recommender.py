import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("goodreads_books.csv")

# Preprocess: Combine genres, description, and authors into a single metadata column
df["metadata"] = df["average_rating"] + " " + df["language_code"] + " " + df["authors"]

# Vectorize metadata
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["metadata"])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = df[df["title"] == title].index[0]
    except IndexError:
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 recommendations (exclude itself)
    book_indices = [i[0] for i in sim_scores]
    return df[["title", "authors", "average_rating"]].iloc[book_indices]