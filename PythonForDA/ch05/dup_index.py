import pandas as pd
import numpy as np
obj = pd.Series(range(5), index=list('aabbc'))
obj
obj.index
obj.index.is_unique()
obj.index.is_unique
obj['a']
obj['b']
df = pd.DataFrame(np.random.randn(4, 3), index=list('aabb'))
df
df.loc['a']
df.loc['b']
