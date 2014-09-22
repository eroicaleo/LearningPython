#!/usr/bin/env python3

import dir1.dir2.mod

print(dir1)
print(dir1.dir2)
print(dir1.dir2.mod)

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

from dir1.dir2 import mod
print(mod.z)
from dir1.dir2.mod import z
print(z)
import dir1.dir2.mod as mod
print(mod.z)
from dir1.dir2.mod import z as modz
print(modz)


