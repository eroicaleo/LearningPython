"""

    >>> from collections import abc
    >>> issubclass(tuple, abc.Sequence)
    True
    >>> issubclass(list, abc.MutableSequence)
    True

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()