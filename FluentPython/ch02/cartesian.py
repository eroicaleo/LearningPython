#!/usr/bin/env python

colors = ['white', 'black']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for size in sizes
                         for color in colors ]
print(tshirts)

tshirts = [(color, size) for color in colors
                         for size in sizes ]
print(tshirts)
