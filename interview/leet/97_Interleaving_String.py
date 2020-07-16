#!/usr/bin/env python

# s1 = 'aabcc'
# s2 = 'dbbca'
# s3 = 'aadbbcbcac'

#   Ф a a b c c
# Ф 1 1 1 0 0 0
# d 0 0 1 1 0 0
# b 0 0 1 1 1 0
# b 0 0 1 0 1 0
# c 0 0 1 1 1 0
# a 0 0 0 0 1 1


class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        curr, prev = [0]*(1+len(s1)), [1]+[0]*len(s1)
        for j in range(0, 1+len(s2)):
            curr[0] = int(j==0) or prev[0]*(s3[j-1]==s2[j-1])
            for i in range(1, 1+len(s1)):
                print(f'{i}, {j}')
                curr[i] = (j>0 and int(prev[i]*(s3[i+j-1]==s2[j-1])) or curr[i-1]*(s3[i+j-1]==s1[i-1]))
            curr, prev = [0]*(1+len(s1)), curr
            print(f'{prev}')
        return (prev[-1] == 1)

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbbaccc'
s3 = 'aadbbcbcac'
s1 = 'a'
s2 = ''
s3 = 'a'
sol = Solution()
print(sol.isInterleave(s1, s2, s3))
