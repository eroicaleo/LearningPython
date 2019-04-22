#!/usr/bin/env python

class Solution:
    def longestValidParentheses(self, s):
        from collections import deque
        maxlen, stack = 0, deque([0])
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                currlen = stack.pop()
                if len(stack) == 0:
                    stack.append(0)
                else:
                    stack[-1] += currlen+2
                maxlen = max(maxlen, currlen)
            print(stack)
        while len(stack) > 0:
            maxlen = max(maxlen, stack.pop())
        return maxlen

sol = Solution()
s = ')()())'
s = '(()'
s = ")(((((()())()()))()(()))("
print(sol.longestValidParentheses(s))
