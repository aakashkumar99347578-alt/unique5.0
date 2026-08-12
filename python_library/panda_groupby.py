import numpy as np
import pandas as pd

movies = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\imdb-top-1000.csv')
print(movies)

# how to created group using single coloumn.

print("-------------------------------------how to created group using single coloumn---------------------------------")
genres = movies.groupby('Genre')

# Applying builtin aggregation fuctions on groupby objects

print("----------------------------applying builtin aggregation functions on groupby objects----------------------------------")
print(genres)
print(genres.std(numeric_only=True))

# find the top 3 genres by total earning

print("---------------------------------find the top 3 genres by total earning---------------------------------------------")
print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))

# find director with most popularity

print("-----------------------------------------find director with most popularity----------------------------------------")
print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

# find the highest rated movie of each genre

print("------------------------find the highest rated movie of each genre------------------------------")
print(movies.groupby('Genre')['IMDB_Rating'].max())

# find number of movies done by each actor

print("---------------------------find number of movies done by each actor-----------------------------------------")
print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

# GroupBy Attributes and Methods -> 
print("-----------groupby attributes and methods---------------------------")


# find total number of groups -> len

print("--------------------find total number of groups-------------------")
print(len(movies.groupby('Genre')))

# find items in each group -> size

print("--------------find items in each group---------------------------------")
print(movies.groupby('Genre').size())

# first()/last() -> nth item

print("-------------------first()/last()-> nth item-------------------------------------")
genres = movies.groupby('Genre')
print(genres.first())
print(genres.last())
print(genres.nth(6))

# get_group -> vs filtering

print("----------------get_group -> vs filtering--------------------------------------------------")
print(genres.get_group('Fantasy')) # get_group
print(movies[movies['Genre'] == 'Fantasy']) # filtering

# groups -> groups return every group wise index data.

print("-----------------------------------------------groups------------------------")
print(genres.groups)

# describe

print("------------------------------------------describe----------------------------------------")
print(genres.describe())

# sample

print("----------------------------------sample-----------------------------------------------------------")
print(genres.sample(2,replace=True))

# nunique

print("-----------------------------------nunique---------------------------")
print(movies['Genre'].nunique())

# agg method ->
# passing dict

print("------------------------------------agg method through the dictionary----------------------------------")
print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))

# list 

print("--------------------------------------agg method through the list---------------------------------")
#print(genres.agg(['min','max','mean','sum']))

# Adding both the syntax

print("----------------------------adding both the syntax-----------------------------------")
print(genres.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
))

# looping on groups

print("--------------------------------------looping on groups---------------------------------------------")
df = pd.DataFrame(columns=movies.columns)

for group, data in genres:
    df = pd.concat([
        df,
        data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]
    ])

print(df)

# find number of movies starting with A for each group

print("-----------------find number of movies starting with A for each group-----------------------------------------------")
def foo(group):
  return group['Series_Title'].str.startswith('A').sum()
print(genres.apply(foo))

# find ranking of each movie in the group according to IMDB score

print("-----------------------------find ranking of each movie in the group according to IMDB score---------------")
def rank_movie(group):
  group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
  return group
print(genres.apply(rank_movie))

# find normalized IMDB rating group wise

print("---------------------------------------find normalized IMDB rating group wise------------------------------------------")
def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group

genres.apply(normal)

# GROUPBY ON MULTIPLE COLS

print("-----------------------GROUP ON MULTIPLE COLS-----------------------------------")
duo = movies.groupby(['Director','Star1'])
print(duo)
# size

print("----------------------------------SIZE------------------------------------------------")
print(duo.size())

# get_group

print("---------------------------get_group-------------------------------")
print(duo.get_group(('Aamir Khan','Amole Gupte')))

# find the most earning actor->director combo

print("-------------------------------find the most earning actor -> director combo-------------------------------------")
print(duo['Gross'].sum().sort_values(ascending=False).head(1))

# find the best(in-terms of metascore(avg)) actor->genre combo

print("--------------------------find the best(in-terms of metascore(avg))actor -> genre combo------------------------------")
print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1))

# agg on multiple 

print("------------------------agg on multiple groups---------------------------------")
print(duo.agg(['min','max','mean']))


