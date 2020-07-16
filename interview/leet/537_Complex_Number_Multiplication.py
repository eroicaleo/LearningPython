#!/usr/bin/env python

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_l, b_l = a.split('+'), b.split('+')
        ar, ai = int(a_l[0]), int(a_l[1][:-1])
        br, bi = int(b_l[0]), int(b_l[1][:-1])
        print(ar, ai, br, bi)
        return f'{ar*br-ai*bi}+{ar*bi+ai*br}i'

a, b = "1+-1i", "1+-1i"
a, b = "1+1i", "1+1i"
sol = Solution()
print(sol.complexNumberMultiply(a, b))
