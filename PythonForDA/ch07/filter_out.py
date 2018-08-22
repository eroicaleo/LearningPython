import numpy as np
from numpy import nan as NA
import pandas as pd
data = pd.Series([1, NA, 3.5, NA, 7])
data
data.dropna()
data.notnull()
data[data.notnull()]
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
data
cleaned
cleaned = data.dropna(how='all')
cleaned
data[4] = NA
data
data.dropna(how='all', axis=1)
df = pd.DataFrame(np.random.randn(7,3))
df
df.iloc[:4, 1] = NA
df
df.iloc[:2, 2] = NA
df
df.dropna()
df.dropna(thresh=2)
