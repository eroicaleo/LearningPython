#!/usr/bin/env python

class Solution:
    def wordBreak(self, s, wordDict):
        length, prev, curr = len(s), [False] * len(s), [False] * len(s)
        prev[0], next_start = True, 0
        while next_start < length:
            # main DP
            i, next_start = next_start, length
            while i < length:
                if prev[i]:
                    for w in wordDict:
                        print('i = %d, w = %s, s[i:len(w)] = %s' % (i, w, s[i:i+len(w)]))
                        if i+len(w) == length and s[i:i+len(w)] == w:
                            return True
                        if i+len(w) <  length and s[i:i+len(w)] == w and (not prev[i+len(w)]):
                            curr[i+len(w)], next_start = True, min(i+len(w), next_start)
                i += 1
            print(prev, curr, 'next_start = %d' % next_start)
            prev, curr = curr, [False] * length
        return False

s, wordDict = 'leetcode', ['leet', 'code']
s, wordDict = 'applepenapple', ['apple', 'pen']
s, wordDict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s, wordDict = 'goalspecial', ['go', 'goal', 'goals', 'special']

sol = Solution()
print(sol.wordBreak(s, wordDict))
