#!/usr/bin/env python

class Solution:
    def generateParenthesis(self, n):
        def gen(lp, rp):
            if not lp:
                return [rp]
            ret = ['(' + s for s in gen(lp[1:], rp)]
            if len(rp) > len(lp):
                ret += [')' + s for s in gen(lp, rp[1:])]
            return ret
        return gen('('*n, ')'*n)

sol = Solution()
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
ret = sol.generateParenthesis(4)
set1 = set(ret)
set2 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
print(set2-set1)
print(len(set(ret)))
print(sorted(ret))
