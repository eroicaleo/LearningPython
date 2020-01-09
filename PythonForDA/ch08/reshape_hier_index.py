import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio','Colorado'], name='state'),)
pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio','Colorado'], name='state'))
pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio','Colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name='number'))
data = pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio','Colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name='number'))
data
result = data.stack()
result
result.index
result.unstack()
result
result.unstack(0)
result.unstack(1)
results
result
result.unstack('state')
s1 = pd.Series([0,1,2,3], index=list('abcd'))
s1
s1 = pd.Series([4,5,6], index=list('abc'))
s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('abc'))
s1, s2
s2 = pd.Series([4,5,6], index=list('cde'))
s2
pd.concat(s1, s2)
pd.concat([s1, s2])
pd.concat([s1, s2], axis=1)
?pd.concat
pd.DataFrame(pd.concat([s1, s2], axis=1))
pd.DataFrame(pd.concat([s1, s2], axis=1), columns=['lala', 'haha'])
df1 = pd.DataFrame(pd.concat([s1, s2], axis=1))
df1
df1.columns = list('ab')
df1
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2
data2.unstack()
data2.unstack().stack()
data2.iloc[1]
data2.unstack().iloc[1]
data2.unstack().iloc[1,'a']
data2.unstack().iloc[1]['a']
data2.unstack().loc[1, 'a']
data2.unstack().loc['one', 'a']
data2.unstack().loc['two', 'a']
data2.unstack().stack(dropna=False)
result
result + 5
pd.DataFrame({'left': result, 'right': result+5})
pd.DataFrame({'left': result, 'right': result+5}, columns=pd.Index(['left', 'right'], name='side'))
df = pd.DataFrame({'left': result, 'right': result+5}, columns=pd.Index(['left', 'right'], name='side'))
df.unstack('state')
df.unstack('state').stack('side')
df
