#!/usr/bin/env python

import collections

class Solution:
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
        for o in l:
            if o in list('+-') and len(d) == 3:
                o2, operator, o1 = d.pop(), d.pop(), d.pop()
                res = o1 + o2 if operator == '+' else o1-o2
                d.append(res)
                d.append(o)
            elif (o not in list('+-*/')) and (len(d) > 1) and (d[-1] in list('*/')):
                operator, o1 = d.pop(), d.pop()
                res = o1*o if operator == '*' else o1//o
                d.append(res)
            else:
                d.append(o)
            print(d)
        if len(d) == 3:
            o2, operator, o1 = d.pop(), d.pop(), d.pop()
            res = o1 + o2 if operator == '+' else o1-o2
            d.append(res)
        print(d)
        return d.pop()

sol = Solution()
s = ' 30+6 / 2'
s = ' 3+5 / 2'
s = ' 3/2'
s = '3+2*2'
s = '14/3*2'
print(sol.calculate(s))

d = collections.deque([1,2,3])
