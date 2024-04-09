import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'netflix_shows.csv'  # Ensure this path is correct and accessible from the script's location
netflix_shows = pd.read_csv(file_path)

# Filter the dataset for shows released in 2021
shows_2021 = netflix_shows[netflix_shows['release_year'] == 2021]

# Counting the number of shows for all countries in 2021, considering shows may list multiple countries
country_counts_all_2021 = shows_2021['country'].str.split(', ').explode().value_counts()

# Limit to the top 10 countries...
top_10_countries_2021 = country_counts_all_2021.head(10)

plt.figure(figsize=(12, 12)) 
plt.pie(top_10_countries_2021, labels=top_10_countries_2021.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
plt.title('Top 10 Countries for Netflix Shows Released in 2021')
plt.show()
