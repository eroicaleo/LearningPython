s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=list(acde))
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=list('acde'))
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1
s2
s1 + s2
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1 + df2
df1 = pd.DataFrame({'A': [1, 2]})
df1
df1 = pd.DataFrame({'B': [3, 4]})
 df1 = pd.DataFrame({'A': [1, 2]})
df2 =  pd.DataFrame({'B': [3, 4]})
df1, df2
df1
df2
df1 + df2
df1 - df2
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df1
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1
df2
df2.loc[1, 'b']
df2.loc[1, 'b'] = np.nan
df2
df1 + df2
df1.add(df2, fill_value = 0)
1 / df1
df1.rdiv(1.)
df1.reindex(columns=df2.columns, fill_value=0.0)
