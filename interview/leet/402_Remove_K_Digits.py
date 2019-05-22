#!/usr/bin/env python3

'''
The thinking process:
Assume num[i], num[i+1] is the first pair s.t.
num[i] > num[i+1], then num[i] must be removed in the
final optimal solution.
If not, keep any one of the removed numbers, and remove num[i] 
the obtained number is smaller
'''

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        from collections import deque
        removed = 0
        stack = deque()
        ret = ''
        for d in num:
            while removed < k and stack and stack[-1] > d:
                stack.pop()
                removed += 1
            stack.append(d)
        while removed < k:
            stack.pop()
            removed += 1
        while stack and stack[0] == '0':
            stack.popleft()
        while stack:
            ret += stack.popleft()
        return ret or '0'

sol = Solution()
num, k = "1432219", 3
num, k = "10200", 1
num, k = "10", 2
num, k = "9", 1
print(sol.removeKdigits(num, k))
