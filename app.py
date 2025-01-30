import streamlit as st
import pandas as pd
from recommender import get_recommendations

# Load the dataset to display book titles
df = pd.read_csv("goodreads_books.csv")
titles = df["title"].tolist()

# Streamlit UI
st.title("📚 Book Recommendation Engine")
st.write("Enter a book you like, and we'll suggest similar books!")

# Dropdown for selecting a book
selected_title = st.selectbox("Choose a book:", titles, index=None, placeholder="Please enter a book/select")

# Button to trigger recommendations
if st.button("Recommend"):
    if selected_title:
        recommendations = get_recommendations(selected_title)
        if not recommendations.empty:
            st.subheader("Recommended Books:")
            for idx, row in recommendations.iterrows():
                st.write(f"**{row['title']}** by *{row['authors']}* (Rating: {row['average_rating']}/5)")
        else:
            st.error("No recommendations found. Try another book!")
    else:
        st.warning("Please select a book first!")