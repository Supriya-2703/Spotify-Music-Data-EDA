## 🎵 Spotify Music Dataset — Exploratory Data Analysis (EDA)

This project performs an in-depth Exploratory Data Analysis (EDA) on a Spotify music dataset to uncover trends in audio features such as tempo, energy, danceability, loudness, and popularity.
It also includes an interactive Streamlit dashboard for exploring patterns across genres and musical attributes.

![Streamlit UI](https://img.shields.io/badge/Made%20With-Streamlit-red?logo=streamlit)
 
![spotify_eda_banner](images/spotify_eda_banner.png)

## 📌 Features of the Project
## 🔍 1. Data Cleaning & Preprocessing

- Handling missing values
- Dropping irrelevant features
- Converting data types
- Saving final cleaned dataset (dataset_cleaned.csv)

## 📊 2. Exploratory Data Analysis (EDA)

- Includes visual analysis of:
- Tempo distribution
- Popularity distribution
- Genre-wise popularity comparison
- Correlation heatmap
- Feature vs Popularity plots
- Insights on what makes songs popular

## 🧠 3. Insights

- Danceability and energy often have strong correlations with popularity
- Tempo has weak correlation with popularity
- Genre plays an important role in determining popularity
- Some features show multicollinearity (e.g., loudness vs energy)

## 🖥 4. Interactive Dashboard (Streamlit)

- Built using Streamlit to explore:
- Popularity distribution by genre
- Correlation heatmap
- Interactive feature-vs-popularity scatter plots
- Sidebar filters for selecting genres & features

Run the dashboard:
streamlit run spotify_dashboard.py

## 📁 Project Structure
📦 Spotify-EDA-Project

├── dataset.csv                    
├── dataset_cleaned.csv      
├── spotify_dashboard.py           
├── Notebook.ipynb         
├── requirement.txt    
└── README.md                      

## 🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

Or manually install:
pip install pandas numpy matplotlib streamlit

2️⃣ Run EDA in Jupyter Notebook
Open eda_notebook.ipynb and run all cells.

3️⃣ Launch Dashboard
streamlit run spotify_dashboard.py

## 🌟 Project Summary

This project explores the patterns behind Spotify music trends using clear visualizations and interactive tools. It reveals how audio features and genres influence the popularity of songs, helping understand the “science” behind hit tracks.
The Streamlit dashboard provides a simple and intuitive way to interact with the data and visualize insights in real time.

## 📌 Future Enhancements

- Build a machine learning model to predict popularity
- Add more interactive visualizations using Plotly
- Add clustering to group similar songs
- Deploy dashboard online (Streamlit Cloud / HuggingFace)

## 📃 License
This project is licensed under the MIT License – see the LICENSE file for details.
