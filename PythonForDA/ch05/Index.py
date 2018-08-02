obj = pd.Series(range(3), index=list('abc'))
obj
index = obj.index
index
index[1:]
index[1] = 'd'
label = pd.Index(range(3))
label
label = pd.Index(np.arange(3))
label
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
obj2 = pd.Series([1.5, -2.5, 0], index=label)
obj2
frame3
frame3.columns
'Ohio' in frame3.columns
2003 in frame3.index
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
dup_labels
