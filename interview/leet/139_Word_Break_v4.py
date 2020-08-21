#!/usr/bin/env python

class Solution:
    def wordBreak(self, s, wordDict):
        mem = {'': [[]]}
        def dfs(rest):
            if not rest in mem:
                mem[rest] = [[w]+l for w in wordDict if rest.startswith(w) for l in dfs(rest[len(w):])]
            return mem[rest]
        return [' '.join(c) for c in dfs(s)]
        # return dfs([], s)

    def wordBreak2(self, s, wordDict):
        def dfs(rest, mem):
            print(f'entering: mem[{rest}] = {mem.get(rest, None)}')
            if not rest in mem:
                mem[rest] = [[w]+l for w in wordDict if rest.startswith(w) for l in dfs(rest[len(w):], mem)]
            print(f'leaving: mem[{rest}] = {mem.get(rest, None)}')
            return mem[rest]
        return [' '.join(c) for c in dfs(s, {'': [[]]})]

    def wordBreak3(self, s, wordDict):
        def dfs(rest, mem):
            return mem[rest] if rest in mem else mem.setdefault(rest, [(w+' '+l).rstrip() for w in wordDict if rest.startswith(w) for l in dfs(rest[len(w):], mem)]) 
        return dfs(s, {'': ['']})
 
s, wordDict = 'leetcode', ['leet', 'code']
s, wordDict = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
s, wordDict = 'catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']
s, wordDict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s, wordDict = 'applepenapple', ['apple', 'pen']
sol = Solution()
print(sol.wordBreak3(s, wordDict))
d = {}
d['a'] = []
print(d.setdefault('a', 'lala'))
# print({'':[[]]})
# print(['word']+[])
