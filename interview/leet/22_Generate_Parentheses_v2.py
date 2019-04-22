#!/usr/bin/env python

# Based on Stefan
class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p+'(', left-1, right): yield q
                for q in generate(p+')', left, right-1): yield q
        return list(generate('', n, n))

sol = Solution()
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
ret = sol.generateParenthesis(4)
set1 = set(ret)
set2 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
print(set2-set1)
print(len(set(ret)))
print(sorted(ret))
