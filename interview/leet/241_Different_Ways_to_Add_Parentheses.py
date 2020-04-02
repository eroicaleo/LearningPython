#!/usr/bin/env python

import re

class Solution:
    def diffWaysToCompute(self, input):
        ret = []
        print(input)
        for i, c in enumerate(input):
            if c in '+-*':
                ops1, ops2 = self.diffWaysToCompute(input[:i]), self.diffWaysToCompute(input[i+1:])
                for o1 in ops1:
                    for o2 in ops2:
                        if c == '+':
                            ret.append(o1+o2)
                        elif c == '-':
                            ret.append(o1-o2)
                        else:
                            ret.append(o1*o2)
        return ret or [int(input)]

input = '2*3-4*5'
input = '2-1-1'
sol = Solution()
print(sol.diffWaysToCompute(input))
