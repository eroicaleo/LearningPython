#!/usr/bin/env python3

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            current_dict = self.trie
            for c in word:
                current_dict = current_dict.setdefault(c, {})
            current_dict['$'] = None

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        print(f'I am searching {word}')
        # if self.search_helper(word, self.trie):
        #     return False
        for i in range(len(word)):
            print(word[:i+1], word[i+1:])
            sub_trie = self.get_sub_trie(word[:i+1])
            print(f'sub_trie = {sub_trie}')
            if any(self.search_helper(word[i+1:], w) for w in sub_trie if w):
                return True
        return False

    def get_sub_trie(self, word):
        sub_trie = self.trie
        for c in word[:-1]:
            if not c in sub_trie:
                return []
            sub_trie = sub_trie[c]
        return [sub_trie[k] for k in sub_trie if k != word[-1]]

    def search_helper(self, word, sub_trie):
        print(f'search_helper word = "{word}", sub_trie = {sub_trie}')
        for c in word:
            print(f'search_helper c = "{c}", sub_trie = {sub_trie}')
            if not c in sub_trie:
                return False
            sub_trie = sub_trie[c]
        print(f'search_helper final sub_trie = {sub_trie}')
        return '$' in sub_trie

d = ['hello', 'hallo', 'leetcode']
d = ['hello', 'leetcode', 'l']

m = MagicDictionary()
m.buildDict(d)
# print(m.search('hello'))
# print(m.search('iello'))
# print(m.search('hillo'))
# print(m.search('heilo'))
# print(m.search('helio'))
# print(m.search('helli'))
# print(m.search('hilli'))
# print(m.search('l'))
# print(m.search('a'))
# print(m.search('leetcoded'))
# print('$' in ['$$'])
# print(m.search('leet'))
# print(m.search('leetcode'))
# print(m.search('lh'))
# print(m.search('l'))
# print(m.get_sub_trie('l'))
