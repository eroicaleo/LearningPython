#!/usr/bin/env python3

class Solution:
    def calculate(self, s: str) -> int:
        self.index, l = 0, len(s)
        def dfs():
            n, res, last_op = 0, 0, '+'
            while self.index < l:
                c, self.index = s[self.index], self.index+1
                if c.isdigit():
                    n = 10*n+int(c)
                elif c == '+' or c == '-':
                    n, res, last_op = 0, res+n if last_op == '+' else res-n, c
                elif c == "(":
                    n = dfs()
                elif c == ")":
                    break
            return res+n if last_op == '+' else res-n
        return dfs()

    def calculate_iter(self, s: str) -> int:
        stack = []
        n, res, last_op = 0, 0, '+'
        for c in s:
            if c.isdigit():
                n = 10*n+int(c)
            elif c == '+' or c == '-':
                n, res, last_op = 0, res+n if last_op == '+' else res-n, c
            elif c == "(":
                stack += [res, last_op]
                n, res, last_op = 0, 0, '+'
            elif c == ")":
                res += (n if last_op == '+' else -n)
                n, last_op, res = res, stack.pop(), stack.pop()
        return (res + (n if last_op == '+' else -n))

sol = Solution()
s = '(1+(4+5+2)-3)+(6+8)'
s = '1 + 1'
s = ' 2-1 + 2 '
print(sol.calculate_iter(s))
