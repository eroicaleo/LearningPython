#!/usr/bin/env python3

class WordDictionary:

    def __init__(self):
        self.trie = {}
 
    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            curr = curr.setdefault(c, {})
        curr['$'] = '$'

    def search(self, word: str) -> bool:
        # return self.search_recursive(word, self.trie)
        return self.search_iterative(word)

    def search_recursive(self, word, path):
        if word == '':
            return '$' in path
        if word[0] == '.':
            return any(self.search_recursive(word[1:], path[k]) for k in path if k != '$')
        else:
            return (word[0] in path) and self.search_recursive(word[1:], path[word[0]])

    def search_iterative(self, word):
        nodes = [self.trie]
        for c in word:
            new_nodes = []
            for node in nodes:
                if c in node:
                    new_nodes += [node[c]]
                elif c == '.':
                    new_nodes += [node[k] for k in node if k != '$']
            nodes = new_nodes
        return any('$' in node for node in nodes)

w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")

word_list = ['bad', 'bada', 'ba', 'pad', '.ad', 'b..', 'b.', 'b.c']

for word in word_list:
    print(f'w.search({word}) = {w.search(word)}')

w = WordDictionary()
w.addWord("a")
w.addWord("a")
word_list = ['.a', 'a.']
print(w.trie)
for word in word_list:
    print(f'w.search({word}) = {w.search(word)}')


