#!/usr/bin/env python3

class Solution:
    def wordBreak(self, s, wordDict):
        # DP part
        dp = [[] for c in s+' ']
        for i in range(len(s)):
            if i == 0 or len(dp[i]) > 0:
                for w in wordDict:
                    if s[i:i+len(w)] == w:
                        dp[i+len(w)].append(i)
            print('i = %d' % i, dp)

        # backtrack part
        def backtrack(index):
            print("I am in backtrack: %d" % index)
            if not dp[index]:
                return ['']
            ret = []
            for k in dp[index]:
                w = s[k:index]
                for wl in backtrack(k):
                    ret.append((wl+" "+w).strip())
            return ret
        return list(filter(len, backtrack(len(s))))

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
sol = Solution()
print(sol.wordBreak(s, wordDict))
