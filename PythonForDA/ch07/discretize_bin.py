import numpy as np
import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cat = pd.cut(ages, bins)
cats
cat
cat.codes
cat.categories
pd.value_counts(cat)
cat = pd.cut(ages, bins, right=False)
cat
cat.categories
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)
data = np.random.rand(20)
data
pd.cut(data, 4, precision=2)
