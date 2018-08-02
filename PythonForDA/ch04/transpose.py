
import numpy as np
arr = np.arange(15).reshape((3,5))
arr
arr.T
arr = np.random.randn(6,3)
arr
np.dot(arr.T, arr)
arr = np.arange(16).reshape((2, 2, 4))
arr
arr.transpose((1, 0, 2))
arr.swapaxes(1, 2)
arr.swapaxes(0, 1)
