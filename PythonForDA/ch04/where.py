xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr)
result
arr = np.random.randn(4,4)
arr
arr > 0
np.where(arr > 0, 2, -2)
np.where(arr > 0, 2, arr)
