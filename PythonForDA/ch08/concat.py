#!/usr/bin/env python3

import numpy as np
import pandas as pd

arr = np.arange(12).reshape((3, 4))

arr = np.arange(12).reshape((3, 4))
np.concatenate([arr, arr], axis=1)
s1 = pd.Series([0,1], index=['a','b'])
s2 = pd.Series([2,3,4], index=['c','d','e'])
s3 = pd.Series([5,6], index=['f','g'])
pd.concat([s1,s2,s3])
pd.concat([s1,s2,s3], axis=1)
pd.concat([s1,s2,s3], axis=1, sort=False)
s4 = pd.concat([s1,s3])
s4
pd.concat([s1,s4])
pd.concat([s1,s4], axis=1)
pd.concat([s1,s4], axis=1, join="inner")
pd.concat([s1,s4], axis=1, join_axes=['a'])
pd.concat([s1,s4], axis=1, join_axes=[['a']])
pd.concat([s1,s4], axis=1, join_axes=[['a', 'c']])
pd.concat([s1,s4], axis=1, join_axes=[['a', 'c', 'b']])
s2
pd.concat([s1,s2], axis=1, join_axes=[['a', 'c', 'b']])
pd.concat([s1,s2,s3])
pd.concat([s1,s2,s3],keys=['lala','haha','kaka'])
result = pd.concat([s1,s2,s3],keys=['lala','haha','kaka'])
result
result.unstack()
pd.concat([s1,s2,s3],keys=['lala','haha','kaka'], axis=1)
df1 = pd.DataFrame(np.arange(6))
df1
df1 = pd.DataFrame(np.arange(6).reshape((3,2)))
df1
pd.DataFrame(np.arange(6).reshape((3,2)), index=list('abc'))
pd.DataFrame(np.arange(6).reshape((3,2)), index=list('abc'), columns=['one', 'two'])
df1 = pd.DataFrame(np.arange(6).reshape((3,2)), index=list('abc'), columns=['one', 'two'])
df2 = pd.DataFrame(np.arange(4).reshape((2,2)), index=list('ac'), columns=['three', 'four'])
df2
np.concat([df1, df2])
pd.concat([df1, df2])
pd.concat([df1, df2]).sort_index(axis=1)
pd.concat([df1, df2]).sort_index(axis=0)
pd.concat([df1, df2]).sort_index(axis=1)
pd.concat([df1, df2]).loc[['one']]
pd.concat([df1, df2])
['one']
pd.concat([df1, df2])['one']
pd.concat([df1, df2])[['one','two']]
df1, df2
df1
df2
pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
pd.concat({'level1':df1, 'level2':df2}, axis=1)
pd.concat({'level1':df1, 'level2':df2})
pd.concat({'level1':df1, 'level2':df2}, axis=1, names=['upper','lower'])
pd.concat({'level1':df1, 'level2':df2}, names=['upper','lower'])
df1 = pd.DataFrame(np.random.randn(3,4), columns=list('abcd'))
df1
df2 = pd.DataFrame(np.random.randn(2,3), columns=list('bda'))
pd.concat([df1,df2])
pd.concat([df1,df2], ignore_index=True)
