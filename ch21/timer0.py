#!/usr/bin/env python3

import time

def timer(func, *args):
    start = time.clock()
    for i in range(10000):
        func(*args)
    return time.clock() - start;
