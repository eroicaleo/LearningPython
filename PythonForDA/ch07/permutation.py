import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5*4).reshape(5,4))
df
sampler = np.random.permutation(5)
sampler
df.take(sampler)
sampler_col = np.random.permutation(4)
sampler_col
sampler_col = np.random.permutation(4)
sampler_col
df[sampler_col]
df.sample(3)
df.sample(3, axis=0)
df.sample(3, axis=1)
df.sample(5)
choice = pd.Series([5,7,-1,6,4])
choice.sample(10, replace=True)
choice.sample(10, replace=True)
