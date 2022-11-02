#!/usr/bin/env python

"""
>>> lax_coordinates = (33.9425, -118.408056)
>>> latitude, longitude = lax_coordinates
>>> latitude
33.9425
>>> longitude
-118.408056
>>> divmod(20, 8)
(2, 4)
>>> t = (20, 8)
>>> divmod(*t)
(2, 4)
>>> quotient, remainder = divmod(*t)
>>> quotient
2
>>> remainder
4
>>> import os
>>> _, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
>>> filename
'id_rsa.pub'
"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# print(divmod(20, 8))
# t = (20, 8)
# print(divmod(*t))
# quotient, remainder = divmod(*t)
# print(quotient, remainder)
#
# import os
# _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# print(filename)
#
# a, b, *rest = range(5)
# print(a, b, rest)
# a, b, *rest = range(3)
# print(a, b, rest)
# a, b, *rest = range(2)
# print(a, b, rest)
# a, *body, c, d = range(5)
# print(a, body, c, d)
# *head, b, c, d = range(5)
# print(head, b, c, d)
