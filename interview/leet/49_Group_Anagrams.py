#!/usr/bin/env python

class Solution:
    def groupAnagrams(self, strs):
        wordDict, ret = {}, []
        for s in strs:
            key = ''.join(sorted(s))
            if not key in wordDict:
                wordDict[key] = [s]
            else:
                wordDict[key].append(s)
        for key in wordDict:
            ret.append(wordDict[key])
        return ret

sol = Solution()
strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(sol.groupAnagrams(strs))
