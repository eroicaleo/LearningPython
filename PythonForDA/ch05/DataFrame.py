import pandas as pd
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame
frame.head()
frame = pd.DataFrame(data, columns=['year', 'state'])
frame
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
frame
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
frame
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
frame
frame.columns
frame.year
frame['state']
frame['pop']
frame['debt']
frame[2]
frame.loc('three')
frame.loc['three']
frame.debt = 1.6
frame
frame.debt = np.arange(6)
frame
frame.debt = np.arange(6.)
frame
frame[0, debt]
frame[0, 'debt']
frame.debt = np.nan
frame
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val
frame.debt = val
val
frame
frame.state == 'Ohio'
type(frame.state == 'Ohio')
frame['eastern'] = frame.state == 'Ohio'
frame
del frame.eastern
del frame['eastern']
frame
frame.columns
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
pop
frame3 = pd.DataFrame(pop)
frame3
frame3.T
pd.DataFrame(pop, index=[2001, 2002, 2003]
)
pd.DataFrame(pop, index=[2001, 2002])
pd.DataFrame(pop)
pd.DataFrame(pop, index=[2001, 2002])
pop
pd.DataFrame(pop, index=np.array([2001, 2002]))
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
pd.DataFrame(pdata)
frame3
frame3.columns.name = 'state'
frame3
frame3.index.name = 'year'
frame3
frame
frame.values
frame3.values
