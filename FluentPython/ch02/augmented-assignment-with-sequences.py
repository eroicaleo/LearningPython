"""
>>> l = [1, 2, 3]
>>> id1 = id(l)
>>> l *= 2
>>> l
[1, 2, 3, 1, 2, 3]
>>> id2 = id(l)
>>> id1 == id2
True
>>> t = (1, 2, 3)
>>> id1 = id(t)
>>> t *= 2
>>> id2 = id(t)
>>> id1 == id2
False
"""


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
