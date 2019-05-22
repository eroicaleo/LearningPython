#!/usr/bin/env python3

class Solution:
    def palindromePairs(self, words):
        length, ret = len(words), []
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                w = words[i]+words[j]
                if w == w[::-1]:
                    ret.append([i,j])
        return ret

sol = Solution()
words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat"]
print(sol.palindromePairs(words))
