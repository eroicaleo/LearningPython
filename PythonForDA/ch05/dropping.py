obj = pd.Series(np.arange(5.), index=list('abcde'))
obj
obj.drop(['c'])
obj.drop(list('dc'))
data = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
data
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1)
data.drop('two', axis='columns')
data.drop(['two', 'four'], axis='columns')
obj.drop('c')
obj.drop('c', inplace=True)
obj
obj['c'] = 2.0
obj
