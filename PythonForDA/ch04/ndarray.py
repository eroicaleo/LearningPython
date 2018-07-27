# To be pasted in IPython

import numpy as np

data = np.random.randn(2, 3)
print(data)
print(data * 10)
print(data + data)
print(data.dtype)
print(data.shape)

data1 = [6,7,5,8,0,1]
arr1 = np.array(data1)
np.array([6.0, 7.5, 8., 0., 1])

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.dtype

np.zeros(10)
np.zeros((3, 6))
np.empty((2,3,2))
np.full((2,3), 2)

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr1.dtype
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr2.dtype

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(np.float32).dtype

empty_uint32 = np.empty(8, dtype='u4')
empty_uint32
