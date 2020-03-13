#!/usr/bin/env python3

# Example 1:Input:s = "aa"p = "a"Output: falseExplanation: "a" does not match the entire string "aa".
#     a a
#   1 0 0
# a 0 1 0 

# Example 2:Input:s = "aa"p = "*"Output: trueExplanation: '*' matches any sequence.
#     a a
#   1 0 0
# * 0 1 1

# Example 3:Input:s = "cb"p = "?a"Output: falseExplanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#     c b
#   1 0 0
# ? 0 1 0
# a 0 0 0

# Example 4:Input:s = "adceb"p = "*a*b"Output: trueExplanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#   Ф a d c e b
# Ф 1 0 0 0 0 0
# * 1 1 1 1 1 1
# a 0 1 0 0 0 0
# * 0 0 1 1 1 1
# b 0 0 0 0 0 1

# Example 5:Input:s = "acdcb"p = "a*c?b"Output: false
#   Ф a c d c b
# Ф 1 0 0 0 0 0
# a 0 1 0 0 0 0
# * 0 1 1 1 1 1
# c 0 0 1 0 1 0
# ? 0 0 0 1 0 1
# b 0 0 0 0 0 0

class Solution:
    def isMatch(self, s, p):
        last_row, curr_row = [1]+[0]*len(s), [0]*(len(s)+1)
        for c in p:
            curr_row[0] = int(c == '*' and last_row[0])
            for i in range(1, len(curr_row)):
                if c == '*':
                    curr_row[i] = max(last_row[i], last_row[i-1], curr_row[i-1])
                else:
                    curr_row[i] = int(last_row[i-1] and (c in s[i-1]+'?'))
            print(curr_row)
            last_row, curr_row = curr_row, [0]*(len(s)+1)
        return (last_row[-1] == True)

sol = Solution()
s = "cb"
p = "?a"
s = "aa"
p = "*"
s = "aa"
p = "a"
s = "adceb"
p = "*a*b"
s = 'acdcb'
p = 'a*c?b'
print(sol.isMatch(s, p))
