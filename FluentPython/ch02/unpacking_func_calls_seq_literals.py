"""
>>> def func(a, b, c, d, *rest):
...     return a, b, c, d, rest
>>> func(*[1, 2], 3, *range(4, 7))
(1, 2, 3, 4, (5, 6))
>>> *range(4), 4
(0, 1, 2, 3, 4)
>>> [*range(4), 4]
[0, 1, 2, 3, 4]
>>> {*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}
"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()