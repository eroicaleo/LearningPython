#!/usr/bin/env python

import collections
import operator

class Solution:
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    def calculate(self, s):
        l = ['']
        for c in s:
            if c == ' ':
                continue
            elif c in list('+-*/'):
                l[-1] = int(l[-1])
                l += [c, '']
            else:
                l[-1] += c
        l[-1] = int(l[-1])

        d = collections.deque()
        for o in l+['+']:
            if o in list('+-'):
                while len(d) >= 3:
                    o2, operator, o1 = d.pop(), d.pop(), d.pop()
                    d.append(self.operator_dict[operator](o1, o2))
            elif (len(d) > 0) and (d[-1] in list('*/')):
                o = self.operator_dict[d.pop()](d.pop(), o)
            d.append(o)
            print(d)
        return d[0]

sol = Solution()
s = '3+2*2'
s = ' 3/2'
s = ' 3+5 / 2'
s = ' 30+6 / 2'
s = '3-2-1'
s = '14/3*2'
print(sol.calculate(s))

d = collections.deque([1,2,3])

