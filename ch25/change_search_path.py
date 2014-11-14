#!/usr/bin/env python3

import sys

print(sys.path)

try:
    import Recursion
except Exception as e:
    print(e)

sys.path.append('../ch19')

print(sys.path)

try:
    import Recursion
except Exception as e:
    print(e)
