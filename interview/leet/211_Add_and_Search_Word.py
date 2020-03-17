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
            return any(self.search_recursive(word[1:], path[c]) for c in path if c != self.word_end)
            # for c in path:
            #     if c != self.word_end:
            #         ret = ret or self.search_recursive(word[1:], path[c])
            #     if ret:
            #         return ret
            # return ret
        else:
            return (word[0] in path) and self.search_recursive(word[1:], path[word[0]])

    def search_iterative(self, word):
        nodes = [self.word_dict]
        for c in word:
            new_nodes = []
            for n in nodes:
                if c in n:
                    new_nodes.append(n[c])
                elif c == '.':
                    for k in n:
                        if k != self.word_end:
                            new_nodes.append(n[k])
            nodes = new_nodes
        return any(self.word_end in n for n in nodes)

    def search_iterative2(self, word):
        nodes = [self.word_dict]
        for c in word:
            nodes = [kid for n in nodes for kid in 
                            ([n[c]] if c in n else
                             [n[k] for k in n if k != self.word_end] if c == '.' else [])]
        return any(self.word_end in n for n in nodes)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # return self.search_recursive(word, self.word_dict)
        return self.search_iterative2(word)

w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
# print(w.word_dict)
word_list = ['bad', 'bada', 'ba', 'pad', '.ad', 'b..', 'b.', 'b.c']

w = WordDictionary()
w.addWord("a")
w.addWord("a")
word_list = ['.a', 'a.']
print(w.word_dict)
for word in word_list:
    print(f'w.search({word}) = {w.search(word)}')

d = dict(zip(list('abcde'), range(5)))
d[None] = None
print(list(filter(None, d)))
