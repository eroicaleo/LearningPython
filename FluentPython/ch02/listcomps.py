#!/usr/bin/env python
"""
# listcomp.py

>>> symbols = '$¢£¥€¤'
>>> codes = [ord(code) for code in symbols]
>>> codes
[36, 162, 163, 165, 8364, 164]

>>> beyond_ascii = [ord(code) for code in symbols if ord(code) > 127]
>>> beyond_ascii
[162, 163, 165, 8364, 164]

# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii)
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()