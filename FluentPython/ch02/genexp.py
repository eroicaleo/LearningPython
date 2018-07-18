#!/usr/bin/env python

symbols = '$¢£¥€¤'
print(tuple(ord(code) for code in symbols))

import array
print(array.array('I', (ord(code) for code in symbols)))

colors = ['white', 'black']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirt)
