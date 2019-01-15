#!/usr/bin/env python

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret, table = [], dict()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if not seq in table:
                table[seq] = 1
            elif table[seq] == 1:
                table[seq] += 1
                ret.append(seq)
        return ret

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))
