#!/usr/bin/env python

class Truth:
    def __bool__(self): return True

X = Truth()
if X: print('yes!')

class Truth:
    def __bool__(self): return False

X = Truth()
print(bool(X))

class Truth:
    def __len__(self): return 0

if not X: print('no!')

class Truth:
    def __bool__(self): return True
    def __len__(self): return 0

X = Truth()
if X: print('yes!')

class Truth:
    pass

X = Truth()
print(bool(X))
