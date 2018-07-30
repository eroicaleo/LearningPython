names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

names == 'Bob'
data[names == 'Bob']
data[names == 'Bob', 2:]
names != 'Bob'
data[-(names == 'Bob')]
data[~(names == 'Bob')]
data[np.logical_not(names == 'Bob')]
mask = (names == 'Bob') | (names == 'Will')
mask
data[mask]
data[data < 0]
data < 0
data[data < 0] = 0
data
data[names != 'Joe'] = 7
data
