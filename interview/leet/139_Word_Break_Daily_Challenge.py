#!/usr/bin/env python

class Solution:
    def wordBreak(self, s, wordDict):
        mem = {w:[w] for w in wordDict}
        def dfs(rest):
            if not rest in mem:
                mem[rest] = [(w+' '+l) for w in wordDict if rest.startswith(w) for l in dfs(rest[len(w):])]
            return mem[rest]
        return dfs(s)


s, wordDict = 'leetcode', ['leet', 'code']
s, wordDict = 'applepenapple', ['apple', 'pen']
s, wordDict = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
s, wordDict = 'catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']
s, wordDict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
print(sol.wordBreak(s, wordDict))
d = dict(zip(['a'], ['a']))
print(d)
