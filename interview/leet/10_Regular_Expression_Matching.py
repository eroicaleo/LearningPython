#!/usr/bin/env python

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p.startswith('*') or '**' in p:
            return False
        prev_row, curr_row = [1] + [0] * len(s), [1] + [0] * len(s)
        for i, c in enumerate(p):
            print(curr_row)
            if c == '*':
                for j in range(1+len(s)):
                    prev_row[j] = max(prev_row[j], curr_row[j])
                    if j >= 1 and p[i-1] == '.':
                        prev_row[j] = max(prev_row[j], prev_row[j-1])
                    if j >= 2 and (s[j-1] == s[j-2]):
                        prev_row[j] = max(prev_row[j], curr_row[j-1])
            else:
                for j in range(1, 1+len(s)):
                    prev_row[j] = curr_row[j-1] if c == '.' or c == s[j-1] else 0
                prev_row[0] = 0
            prev_row, curr_row = curr_row, prev_row
        print(curr_row)
        return (curr_row[-1] == 1)

s, p = ['aa', '**']
s, p = ["aaa", "ab*ac*a"]
s, p = ['aa', 'a']
s, p = ['aa', 'a*']
s, p = ['', 'a*']
s, p = ['ab', '.*']
s, p = ['mississippi', 'mis*is*p*.']
s, p = ['aab', 'c*a*b']
s, p = ['', '']
sol = Solution()
print(sol.isMatch(s, p))
# print(list(range(5,0,-1)))
# print('**' in 'a*a')
