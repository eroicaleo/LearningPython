import numpy as np
from numpy import nan as NA
import pandas as pd

df.fillna(0)
df.fillna({1: 0.5, 2: 0})
_ = df.fillna(0, inplace=True)
df
df = pd.DataFrame(np.random.randn(6,3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
df
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)
data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())
data.mean()
