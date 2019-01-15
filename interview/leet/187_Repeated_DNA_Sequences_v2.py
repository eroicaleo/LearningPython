#!/usr/bin/env python

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret, table = set(), set()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if not seq in table:
                table.add(seq)
            else:
                ret.add(seq)
        return list(ret)

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))

