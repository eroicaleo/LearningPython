#!/usr/bin/env python3

"""
Homegrown timer tools for function calls
Does total time, best-of time, best-of-totals time
"""

import time, sys

timer = time.clock() if sys.platform[:3] == "win" else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times
    Return total time, last results
    """
    start = timer()
    repslist = list(range(reps))
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest rep among reps return
    return (best time, last results)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed > best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals
    """
    return bestoftotal(reps1, total, reps2, func, *pargs, **kargs)
