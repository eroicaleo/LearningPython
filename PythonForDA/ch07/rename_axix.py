import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
data
transform = lambda x : x[:4].upper()
data.index.map(transform)
data.index = data.index.map(transform)
data
str.title('New York')
data.rename(index=str.title, columns=str.upper)
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})
data
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}, inplace=True)
data
