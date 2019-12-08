#!/usr/bin/env python3

import collections
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        beginNextLevel = {beginWord}
        endNextLevel = {endWord}
        beginGraph, endGraph = collections.defaultdict(set), collections.defaultdict(set) 
        wordLength = len(beginWord)
        wordList = set(wordList)
        intersect_flag = False
        iteration = 0 
        if endWord not in wordList:
            return []
        else:
            wordList.remove(endWord)

        while len(wordList) and (not intersect_flag):
            iteration += 1
            print("iteration: {i:d}".format(i=iteration))
            currdict, nextLevel = collections.defaultdict(set), set()
            if len(beginNextLevel) <= len(endNextLevel):
                print('I am taking begin')
                for word in beginNextLevel:
                    print(word)
                    for c in string.ascii_lowercase:
                        for i in range(wordLength):
                            newWord = word[:i]+c+word[i+1:]
                            if newWord in wordList:
                                nextLevel.add(newWord)
                                currdict[word].add(newWord)
                            if newWord in endGraph:
                                intersect_flag = 1
                                print('We see intersect_flag in begin')
                    print(nextLevel)
                    print(currdict)
                beginNextLevel = nextLevel
                beginGraph.update(currdict)
                print('beginGraph:', beginGraph)

            else:
                print('I am taking end')
                for word in endNextLevel:
                    print(word)
                    for c in string.ascii_lowercase:
                        for i in range(wordLength):
                            newWord = word[:i]+c+word[i+1:]
                            if newWord in wordList:
                                nextLevel.add(newWord)
                                currdict[newWord].add(word)
                            if newWord in beginGraph:
                                intersect_flag = 1
                                print('We see intersect_flag in end')
                    print(nextLevel)
                    print(currdict)
                endNextLevel = nextLevel
                endGraph.update(currdict)
                print('endGraph:', endGraph)
            
            wordList -= nextLevel
            print('wordList after this iteration: {wordList}'.format(wordList=wordList))
        beginGraph.update(endGraph)
        print('final Graph:', beginGraph)

        # step 2 DFS
        self.res = []
        self.dfs(beginGraph, beginWord, [])

        return self.res

    def dfs(self, G, word, currList):
        print('In dfs:', word, currList)
        if word == endWord:
            self.res.append(currList)
        elif word in G:
            for w in G[word]:
                self.dfs(G, w, currList+[word])


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(sol.findLadders(beginWord, endWord, wordList))
