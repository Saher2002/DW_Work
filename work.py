import pandas as pd
import numpy as np

df = pd.read_csv("imdb_top_5000_tv_shows.csv") #read the csv file 
# print(df.columns) #display the rows

df.drop_duplicates(inplace=True)
df.dropna(subset=["endYear"], inplace=True)
df['endYear'] = df['endYear'].astype(int)
df['duration'] = df['endYear'] - df['startYear']
df['rating_100'] = df['averageRating'] * 10
df['rating_category'] = pd.cut(df['averageRating'],
                               bins=[0, 5, 7.5, 10],
                               labels=['Low', 'Average', 'High'])
df['votes_normalized'] = (df['numVotes'] - np.mean(df['numVotes'])) / np.std(df['numVotes'])
dw_ready = df[['primaryTitle', 'startYear', 'endYear', 'duration',
               'averageRating', 'rating_100', 'rating_category',
               'numVotes', 'votes_normalized', 'genres', 'directors']]

# print(df.info())
print(df.columns) 
print(dw_ready.columns) 
# print(dw_ready.describe(include='all'))
# Save the engineered data to a new CSV
dw_ready.to_csv("imdb_dw_ready.csv", index=False)
