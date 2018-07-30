arr = np.empty((8, 4))
arr
for i in range(8):
    arr[i] = i
arr
arr[[4, 3, 0, 6]]
arr[[-3, -5, -7]]
arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
