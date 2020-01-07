#!/usr/bin/env python3

import numpy as np
import pandas as pd

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=list('fedcba'))
a
b = pd.Series(np.arange(len(a)), index=list('fedcba'))
b
b = pd.Series(np.arange(len(a)), index=list('fedcba'), dtype=float64)
b = pd.Series(np.arange(len(a)), index=list('fedcba'), dtype=np.float64)
b
np.where(pd.isnull(a), b, a)
b.combine_first(a)
b[:-2].combine_first(a[2:])
b[:-2]
a
a.combine_first(b)
a[2:]
a[2:].combine_first(b)
a
b[1:]
a.combine_first(b[1:])
a.combine_first(b[1:]).sort_index(ascending=False)
a.combine_first(b)
np.where(pd.isnull(a), a, b)
np.where(pd.isnull(a), b, a)
np.array_equal(np.where(pd.isnull(a), b, a), a.combine_first(b).values())
np.array_equal(np.where(pd.isnull(a), b, a), a.combine_first(b).values)
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],})
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],})
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan], 'b': [np.nan, 2., np.nan, 6.], 'c': range(2, 18, 4)})
df1
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.], 'b': [np.nan, 3., 4., 6., 8.]})
df2
df1.combine_first(df2)

