"""
>>> a = (10, 'alpha', [1, 2])
>>> b = (10, 'alpha', [1, 2])
>>> a == b
True
>>> b[-1].append(99)
>>> a == b
False
>>> b
(10, 'alpha', [1, 2, 99])
"""

def fixed(o):
    """
    >>> tf = (10, 'alpha', (1, 2))
    >>> fixed(tf)
    True
    >>> tf = (10, 'alpha', [1, 2])
    >>> fixed(tf)
    False
    """
    try:
        hash(o)
    except TypeError:
        return False
    return True