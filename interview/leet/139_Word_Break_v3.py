#!/usr/bin/env python

class Solution:
    def wordBreak(self, s, wordDict):
        ok, wordSet = [False] * (len(s)+1), set(wordDict)
        ok[0], length, maxWordLen = True, len(s), max(map(len, wordSet))
        for i in range(1, 1+length):
            ok[i] = False
            for j in range(i-maxWordLen, i):
                if ok[j] and (s[j:i] in wordSet):
                    ok[i] = True
        return ok[-1]

s, wordDict = 'leetcode', ['leet', 'code']
s, wordDict = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
s, wordDict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s, wordDict = 'goalspecial', ['go', 'goal', 'goals', 'special']
s, wordDict = 'a', []
sol = Solution()
print(sol.wordBreak(s, wordDict))
