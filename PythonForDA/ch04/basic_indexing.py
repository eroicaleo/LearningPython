import numpy as np

arr = np.arange(10)
arr

arr[5]
arr[5:8]

arr[5:8] = 12
arr

arr_slice = arr[5:8]
arr_slice
arr_slice[1] = 12345
arr
arr_slice[:] = 64

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
arr2d[0, 2]
arr2d[0][2]

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
old_vals = arr3d[0].copy()
arr3d[0] = 42

arr3d[1, 0]

arr[1:6]
arr2d[:2]
arr2d[:2, 1:]
arr2d[2, :1]
arr2d[:, :1]
arr2d[:, :1].shape
arr2d[:2, 1:] = 0
arr2d
