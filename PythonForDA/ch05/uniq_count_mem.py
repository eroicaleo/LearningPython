import pandas as pd
import numpy as np
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj
obj.unique()
type(obj.unique())
type(obj)
unique = obj.unique()
unique
unique.sort()
unique
obj.value_counts()
pd.value_counts(obj.values)
pd.value_counts(obj.values, sort=False)
obj
pd.value_counts(obj.values, sort=False)
mask = obj.isin(['b', 'c'])
mask
obj[mask]
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pd.Index(unique_vals)
pd.Index(unique_vals).get_indexer(to_match)
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4, 4]})
data.apply(pd.value_counts)
data.apply(pd.value_counts).fillna(0)
pd.DataFrame.fillna?
