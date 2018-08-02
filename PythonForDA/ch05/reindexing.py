obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
obj2 = obj.reindex(list('abcde'))
obj2
obj2 = obj.reindex(list('abdef'))
obj2
obj2 = obj.reindex(list('dcabk'))
obj2
obj2 = obj.reindex(list('abcde'))
obj2
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
obj3.reindex(range(6), method='ffill')
frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=list('abc'), columns=['Ohio', 'Texas', 'California'])
frame
frame2 = frame.reindex(list('abcd'))
frame2
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)
frame.loc[list('abcd'), states]
frame.loc[list('abcd'), states]
