#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        l, r, length = 0, len(s)-1, len(s)
        while True:
            while (l < length) and (not s[l].isalnum()):
                l += 1
            while (r >= 0) and (not s[r].isalnum()):
                r -= 1
            if l >= r:
                break
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

sol = Solution()
s_list = [
'A man, a plan, a canal: Panama',
'race a car',
'race a e-car',
' ',
'---',
'',
]
for s in s_list:
    print(f'"{s}"', sol.isPalindrome(s))
