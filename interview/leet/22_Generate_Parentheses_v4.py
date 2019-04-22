#!/usr/bin/env python

class Solution:
    def generateParenthesis(self, n):
        def gen(p, left, right, parens=[]):
            if left: gen(p+'(', left-1, right, parens)
            if right > left: gen(p+')', left, right-1, parens)
            if not right: parens.append(p)
            return parens
        return gen('', n, n)

sol = Solution()
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
ret = sol.generateParenthesis(4)
set1 = set(ret)
set2 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
print(set2-set1)
print(len(set(ret)))
print(sorted(ret))
