#!/usr/bin/env python

class Solution:
    def wordBreak(self, s, wordDict):
        if len(s) == 0: return True
        ret = False
        for w in wordDict:
            if s.startswith(w):
                ret = ret or self.wordBreak(s[len(w):], wordDict)
        return ret

s, wordDict = 'leetcode', ['leet', 'code']
s, wordDict = 'applepenapple', ['apple', 'pen']
s, wordDict = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']

sol = Solution()
print(sol.wordBreak(s, wordDict))
