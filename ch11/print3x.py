#!/usr/local/bin/python3.3

x = ['spam']
y = 99
z = 'eggs'
print(x, y, z)
print(x, y, z, sep='')
print(x, y, z, sep=',')
print(x, y, z, sep='...', end='!\n')

text = '%s: %-.4f %05d' % ('Result', 3.14159, 42)
print(text)

text = '{0}: {1:<.4f} {2:05d}'.format('Result', 3.14159, 42)
print(text)
