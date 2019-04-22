#!/usr/bin/env python

# Based on Stefan
class Solution:
    def generateParenthesis(self, n, open=0):
        # If there is a mistake, open will be < 0
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')'*open] * (not n)

sol = Solution()
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
ret = sol.generateParenthesis(4)
set1 = set(ret)
set2 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
print(set2-set1)
print(len(set(ret)))
print(sorted(ret))
