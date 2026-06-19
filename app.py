# app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Netflix Dashboard")

st.title("Netflix Content Visualization Dashboard")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Movies vs TV Shows")
st.bar_chart(df['type'].value_counts())

st.subheader("Top 10 Ratings")
st.bar_chart(df['rating'].value_counts().head(10))

country = st.selectbox(
    "Select Country",
    sorted(df['country'].dropna().unique())
)

filtered = df[df['country'] == country]

st.subheader(f"Content from {country}")
st.dataframe(
    filtered[['title','type','release_year']]
)
