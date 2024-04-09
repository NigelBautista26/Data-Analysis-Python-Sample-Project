# First, let's load the uploaded CSV file to understand its structure and contents.
import pandas as pd

# Load the CSV file
file_path = 'netflix_shows.csv'
netflix_shows = pd.read_csv(file_path)

netflix_shows.head(), netflix_shows.info()