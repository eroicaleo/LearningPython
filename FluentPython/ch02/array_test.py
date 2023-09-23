from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

import timeit
cmd = 'floats2.fromfile(fp, 10 ** 7)'
SETUP = '''
from array import array
floats2 = array('d')
fp = open('floats.bin', 'rb')
'''
res = timeit.repeat(cmd, setup=SETUP, number=1, repeat=6)
print(*(f'{x:.3f}' for x in res))

ints = array('b', [9,8,7,6,5,4,3,2,1,0])
print(ints)
sorted_ints = sorted(ints)
print(sorted_ints, type(sorted_ints))
sorted_ints = array(ints.typecode, sorted(ints))
print(sorted_ints, type(sorted_ints))
