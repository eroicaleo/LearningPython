import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index=[['a','a','b','b'],[1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])

data = pd.Series(np.random.randn(9), index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,3,1,2,2,3]])
data
data.index
data['b']
data['b':'c']
data.loc[['b', 'd']]
data.loc[:,2]
data.unstack()
data.unstack().stack()
frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index=[['a','a','b','b'],[1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])
frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
frame['Ohio']
frame[:,'a']
frame.loc[:,'a']
frame.loc['a']
frame
frame.loc['a', 'Ohio']
frame.loc[['a','b'], 'Ohio']
frame[:,'Green']
frame.loc[:,'Green']
frame[[:,'Green']]
frame[['Green']]
frame[['a']]
frame['a']
frame.loc['a']
frame.loc[:, 'Green']
frame
frame.loc[:, [:, 'Green']]
frame.loc[:, 'Ohio']
frame.loc[:, 'Ohio']['Green']
frame.loc[:]['Green']
frame.loc[:, :]['Green']
