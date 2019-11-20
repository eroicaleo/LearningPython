import numpy as np
import pandas as pd

df = pd.DataFrame({'key': ['b','b','a','c','a','b'], 'data1': range(6)})
df
pd.get_dummies(df['key'])
pd.get_dummies(df['key'], prefix='key')
df['data1']
df[['data1']]
dummies = pd.get_dummies(df['key'], prefix='key')
dummies
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy
type(df[['data1']])
type(df['data1'])
?pd.DataFrame.join
?pd.DataFrame.join
pwd
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
movies
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
movies
movies.genres
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
all_genres
genres = pd.unique(all_genres)
genres
zero_matrix = np.zeros(len(movies), len(genres))
zero_matrix = np.zeros((len(movies), len(genres)))
zero_matrix
dummies = pd.DataFrame(zero_matrix, columns=genres)
dummies
dummies.columns
dummies.columns.get_indexer(movies.genres[0].split('|'))
dummies.columns.get_indexer(movies.genres[1].split('|'))
for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

## Thi is dumb method
'''
dummies2 = pd.DataFrame(zero_matrix, columns=genres)
for i, gen in enumerate(movies.genres):
    for ge in gen.split('|'):
        dummies2.loc[i, ge] = 1
'''

dummies
dummies.add_prefix('Genre_')
movies_windic = movies.join(dummies.add_prefix('Genre_'))
movies_windic

## Use with cut
np.random.seed(12345)
values = np.random.rand(10)
type(values)
values
bins = [0,0.2,0.4,0.6,0.8,1]
bins
cats = pd.cut(values, bins)
cats
cats.codes
cats.categories
pd.get_dummies(cats)
