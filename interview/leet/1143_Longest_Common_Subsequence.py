#!/usr/bin/env python3

#   Φ a b c d e 
# Φ 0 0 0 0 0 0
# a 0 1 1 1 1 1
# b 0 1 2 2 2 2
# e 0 1 2 2 2 3

#   Φ b s b i n i n m
# Φ 0 0 0 0 0 0 0 0 0
# j 0 0 0 0 0 0 0 0 0
# m 0 0 0 0 0 0 0 0 1
# j 0 0 0 0 0 0 0 0 1
# k 0 0 0 0 0 0 0 0 1
# b 0 1 1 1 1 1 1 1 1
# k
# j
# k
# v

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        prev, curr = [0]*(len(text1)+1), [0]*(len(text1)+1)
        for c2 in text2:
            for i, c1 in enumerate(text1):
                if c1 == c2:
                    curr[i+1] = prev[i] + 1
                else:
                    curr[i+1] = max(prev[i+1], curr[i])
            prev, curr = curr, [0]*(len(text1)+1)
        return prev[-1]
            

text1 = "abc"
text2 = "abc"
text1 = "bsbininm"
text2 = "jmjkbkjkv"
text1 = "abcde"
text2 = "ace"
text1 = "abc"
text2 = "def"

sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))
