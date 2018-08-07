import numpy as np
import pandas as pd
obj = pd.Series(np.arange(4.), index=list('abcd'))
obj
obj['b']
obj[1]
obj[2:4]
obj[list('bad')]
obj[[1,3]]
obj[obj < 2]
obj['b':'c']
obj['b':'a']
obj['b':'c'] = 5.
obj
data = pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
data
data['two']
data[['three', 'one']]
data['three':'four']
data[['three','four']]
data[:2]
data[data['three'] > 5]
data < 5
data[data < 5] = 0
data
data.loc['Colorado', ['two', 'three']]]
data.loc['Colorado', ['two', 'three']]
data.iloc[2, [3, 0, 1]]
data
data.iloc[2]
data.iloc[[1, 2], [3, 0, 1]]
data.loc[:'Utah', 'two']
data.iloc[:, :3]
data.iloc[:, :3][data.three > 5]
data.three > 5
