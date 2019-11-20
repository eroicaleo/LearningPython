#!/usr/bin/env python3

from itertools import permutations

l = [" ".join(combo) for combo in permutations("Good morning Rosa!".split(), 3)]
print(l)

s =  """Find textbooks with titles containing 'NLP',
        or 'natural' and 'language', or 'computational'
        and 'linguistics'."""
print(len(set(s.split())))

import numpy as np
print(np.arange(1, 12+1).prod())
