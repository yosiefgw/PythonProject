# use to_string() to print the entire DataFrame.
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
import pandas as pd
df = pd.read_csv('world_population.csv')
# print(df.to_string(index=False))
print(df.head(10))
print(df.info())
# Set the index of the data frame as “Continent”
df.set_index('Continent', inplace=True)
# Print out the population data for all countries in Europe
europe_population = df.loc['Europe']
print(europe_population)






