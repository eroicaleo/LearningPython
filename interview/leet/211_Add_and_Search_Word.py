#!/usr/bin/env python3

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = dict()
        self.word_end = '_end_'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current_dict = self.word_dict
        for c in word:
            current_dict = current_dict.setdefault(c, {})
        current_dict[self.word_end] = self.word_end

    def search_recursive(self, word, path):
        if word == '':
            return (self.word_end in path)
        ret = False
        if word[0] == '.':
            for c in path:
                ret = ret or self.search_recursive(word[1:], path[c])
                if ret:
                    return ret
            return ret
        else:
            return (word[0] in path) and self.search_recursive(word[1:], path[word[0]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_recursive(word, self.word_dict)
        # current_dict = self.word_dict
        # for c in word:
        #     if c in current_dict:
        #         current_dict = current_dict[c]
        #     else:
        #         return False
        # return (self.word_end in current_dict)

w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
# print(w.word_dict)
word_list = ['bad', 'bada', 'ba', 'pad', '.ad', 'b..', 'b.', 'b.c']
for word in word_list:
    print(f'w.search({word}) = {w.search(word)}')

# search(".ad") -> true
# search("b..") -> true
