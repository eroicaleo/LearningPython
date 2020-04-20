#!/usr/bin/env python3

from collections import Counter
from functools import reduce
import string
class Solution:
    def countOfAtoms(self, formula):
        self.index, l = 0, len(formula)
        def helper(t, n):
            c = Counter()
            if t:
                c = Counter([t]*n) if isinstance(t, str) else reduce(lambda c1, c2: c1+c2, (t for i in range(n)))
            return c
        def dfs():
            cnt = Counter()
            t, n = '', 1
            while self.index < l:
                self.index, c = self.index+1, formula[self.index]
                if c in string.ascii_lowercase:
                    t += c
                elif c in string.ascii_uppercase:
                    cnt += helper(t, n)
                    t, n = c, 1
                elif c.isdigit():
                    n = int(c) + (0 if n == 1 else 10*n)
                    print(f'See a digit c = {c}, n = {n}')
                elif c == '(':
                    cnt += helper(t, n)
                    print(f'See a "(" t = {t}, cnt = {cnt}')
                    t, n = dfs(), 1
                elif c == ')':
                    break
            return cnt + helper(t, n)
        return ''.join(f'{s}{"" if i == 1 else i}' for s, i in sorted(dfs().items()))

sol = Solution()
formula = 'K4(ON(SO3)2)2'
formula = 'Mg(OH)2'
formula = 'H2O'
print(sol.countOfAtoms(formula))

# print(collections.Counter('aabb')+collections.Counter('ccdd'))
# print(reduce(lambda c1, c2: c1+c2, (collections.Counter('aabb') for i in range(3))))
# cnt_l = [collections.Counter('aabb') for i in range(3)]
# print(cnt_l)
# print(collections.Counter(['Mg']))
