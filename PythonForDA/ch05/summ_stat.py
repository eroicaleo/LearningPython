df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df
df.sum()
df.sum(axis='columns')
df
df.mean(axis='columns', skipna=False)
df.idxmax
df.idxmax()
df.idxmin()
df.cumsum()
df
df.describe
df.describe()
obj = pd.Series(list('aabc'*4))
obj
obj.describe()
