# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

#filtering for movies only 
df_movies = netflix_df[netflix_df['type'] == 'Movie']
df_90s_movies = df_movies[(df_movies['release_year'] >= 1990) & (df_movies['release_year'] < 2000)]

# Find the most frequent movie duration in the 1990s
duration = df_90s_movies['duration'].mode()[0]

# Print the result
print("Most Frequent Movie Duration in the 1990s:", duration)


# Filter for short action movies (< 90 minutes)
short_action_movies = df_90s_movies[(df_90s_movies['duration'] < 90) & (df_90s_movies['genre'] == 'Action')]

# Count the number of short action movies
short_movie_count = short_action_movies.shape[0]

# Print the result
print("Number of Short Action Movies in the 1990s:", short_movie_count)
