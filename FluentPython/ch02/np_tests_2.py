import numpy as np
import os.path

if not os.path.isfile('floats-10M-lines.txt'):
    floats = np.random.rand(10 ** 7,)
    floats.shape
    np.savetxt('floats-10M-lines.txt', floats)
else:
    print(f'Found floats-10M-lines.txt')


floats = np.loadtxt('floats-10M-lines.txt')
print(floats[-3:])
floats *= .5
print(floats[-3:])

from time import perf_counter as pc

t0 = pc(); floats /= 3;
t_dur = pc() - t0
print(f't_dur = {t_dur}')
np.save('floats-10M', floats)
floats2 = np.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])
