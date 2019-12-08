#!/usr/bin/env python3

import collections
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord in wordList:
            return []
        level, wordList = {beginWord}, set(wordList)
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i+1:]
                        if n in wordList:
                            next_level[n].add(node)
            wordList -= next_level.keys()
            level = next_level
            parents.update(next_level)
            # print(level, wordList)
            # print('parents: ', parents)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(sol.findLadders(beginWord, endWord, wordList))
