#!/usr/bin/env python3

class Solution:
    def repeatedSubstringPattern(self, s):
        l = len(s)
        if l == 1:
            return False
        if len(set(s)) == 1:
            return True
        for i in range(2, l//2+1):
            if l % i == 0:
                for j in range(1, l//i):
                    if s[0:i] != s[j*i:(j+1)*i]:
                        break
                else:
                    return True
        return False

    # If we can find s is s1, and index is i in s1
    # Then s[:i+1] is the repeated pattern
    def repeatedSubstringPattern_v2(self, s):
        s1 = s[1:]+s[:-1]
        return s1.find(s) != -1

sol = Solution()
s_list = [
  'abab',
  'aba',
  'abcabcabcabc',
]
for s in s_list:
    print(s, sol.repeatedSubstringPattern(s))
