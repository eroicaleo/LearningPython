"""
>>> import numpy as np
>>> a = np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> type(a)
<class 'numpy.ndarray'>
>>> a.shape
(12,)
>>> a.shape = 3, 4
>>> a # doctest: +NORMALIZE_WHITESPACE
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])
>>> a[2] # doctest: +NORMALIZE_WHITESPACE
array([ 8, 9, 10, 11])
>>> a[2, 1]
9
>>> a[:, 1]
array([1, 5, 9])
>>> a.transpose() # doctest: +NORMALIZE_WHITESPACE
array([[ 0, 4, 8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
