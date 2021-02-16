#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        ret, length = '', len(s)
        for i, c in enumerate(s):
            j = 0
            while j <= i < length-j and s[i-j] == s[i+j]:
                j += 1
            j -= 1
            if len(ret) < 2*j+1:
                ret = s[i-j:i+j+1]
            j = 0
            while j <= i < length-j-1 and s[i-j] == s[i+1+j]:
                j += 1
            if len(ret) < 2*j:
                ret = s[i-j+1:i+j+1]
        return ret

    def bottomup_dp(self, s):
        l, ret = len(s), s[0]
        state = [[0]*l for _ in range(l)]
        state[0][0] = 1
        for i in range(1, l):
            state[i][i] = state[i][i-1] = 1
        for i in range(l-1,-1,-1):
            for d in range(1,l-i):
                if s[i] == s[i+d] and state[i+1][i+d-1]:
                    state[i][i+d] = 1
                    if d+1 > len(ret):
                        ret = s[i:i+d+1]
        return ret

    def bottomup_dp_2(self, s):
        l, ret = len(s), s[0]
        prev = [0]*(l-1)+[1]
        for i in range(l-1,-1,-1):
            curr = [0]*l
            curr[i] = 1
            for d in range(1,l-i):
                if s[i] == s[i+d] and prev[i+d-1]:
                    curr[i+d] = 1
                    if d+1 > len(ret):
                        ret = s[i:i+d+1]
            prev = curr
            prev[i-1] = 1
        return ret



sol = Solution()
# print(sol.longestPalindrome('babad'))
# print(sol.bottomup_dp('babad'))
# print(sol.longestPalindrome('cbbd'))
print(sol.bottomup_dp_2('cbbd'))
print(sol.bottomup_dp_2('babad'))
print(sol.bottomup_dp_2('bb'))
print(sol.bottomup_dp_2('b'))
