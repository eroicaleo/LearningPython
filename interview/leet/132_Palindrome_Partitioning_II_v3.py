#!/usr/bin/env python

# Based on the fasted solution

class Solution:
    def minCut(self, s):
        l = len(s)
        
        # cut[i] means the no. of min cuts of s[:i]
        cut = list(range(-1, l))

        prev = [0]
        for j in range(1, l+1):
            curr = [j]
            for i in prev: # s[i:j] is a palindrome
                cut[j] = min(cut[j], cut[i]+1)
                if j < l:
                    if i > 0 and s[i-1] == s[j]:
                        curr.append(i-1)
                    if i == j-1 and s[i] == s[j]:
                        curr.append(i)
            prev = curr

        return cut[-1]

s = 'abcbad'
s = 'aab'
s = ''
sol = Solution()
print(sol.minCut(s))
