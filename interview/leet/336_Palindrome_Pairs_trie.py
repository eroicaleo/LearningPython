#!/usr/bin/env python3

class Solution:
    def palindromePairs(self, words):
        class TrieNode:
            def __init__(self):
                self.next  = dict()
                self.index = -1
                self.rest  = []

    def addWord(self, root, word, index):
        reverseWord = word[::-1]
        for i, c in enumerate(reverseWord):
            nextRoot = root.next.get(c, TrieNode())
            if reverseWord[i+1:] == reverseWord[i+1:][::-1]:


s = 'abcde'
print(s[::-1][1:])
