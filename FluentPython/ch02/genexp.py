#!/usr/bin/env python

"""

>>> symbols = '$¢£¥€¤'
>>> tuple(ord(code) for code in symbols)
(36, 162, 163, 165, 8364, 164)

>>> import array
>>> array.array('I', (ord(code) for code in symbols))
array('I', [36, 162, 163, 165, 8364, 164])

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']

>>> for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
...     print(tshirt)
black S
black M
black L
white S
white M
white L

"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()