#!/usr/bin/env python3

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        d = collections.defaultdict(int)
        for w in words:
            d[w] += 1
        l = [[] for i in range(len(words)+1)]
        for w in d:
            l[d[w]].append(w)
        ret = []
        for i in range(len(words),0,-1):
            ret += sorted(l[i])
            if len(ret) >= k:
                break
        return ret[:k]


sol = Solution()
words, k = ["i", "love", "leetcode", "i", "love", "coding"], 2
words, k = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
words, k = ["i", "love", "leetcode", "i", "love", "coding"], 1
print(sol.topKFrequent(words, k))
