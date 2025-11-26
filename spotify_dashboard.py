import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset_cleaned.xls")

st.title("**Spotify EDA Dashboard**")
st.write("Explore audio features, genres, and popularity trends.")

# Sidebar Filters
genre_list = df["track_genre"].unique()
selected_genre = st.sidebar.selectbox("Select Genre", genre_list)

filtered_df = df[df["track_genre"] == selected_genre]

st.subheader(f"Popularity Distribution for {selected_genre}")
fig, ax = plt.subplots()
ax.hist(filtered_df["popularity"], bins=30)
st.pyplot(fig)

st.subheader("Correlation Heatmap")
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(8,6))
cax = ax.matshow(corr)
fig.colorbar(cax)
ax.set_xticks(range(len(numeric_cols)))
ax.set_yticks(range(len(numeric_cols)))
ax.set_xticklabels(numeric_cols, rotation=90)
ax.set_yticklabels(numeric_cols)
st.pyplot(fig)

st.subheader("Feature vs Popularity")
feature = st.selectbox("Choose Feature", numeric_cols)

fig2, ax2 = plt.subplots()
ax2.scatter(df[feature], df["popularity"], alpha=0.5)
ax2.set_xlabel(feature)
ax2.set_ylabel("Popularity")
st.pyplot(fig2)

st.write("Dashboard Created Successfully!")
