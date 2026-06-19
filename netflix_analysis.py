# netflix_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# Top 10 Countries
plt.figure(figsize=(10,5))
df['country'].dropna().value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries")
plt.savefig("top_countries.png")
plt.show()

# Top Ratings
plt.figure(figsize=(8,5))
df['rating'].dropna().value_counts().head(10).plot(kind='bar')
plt.title("Content Ratings")
plt.savefig("ratings.png")
plt.show()

# Release Year Trend
plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Released Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("release_year_trend.png")
plt.show()

print("Analysis Completed Successfully")
