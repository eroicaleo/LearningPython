#!/usr/bin/env python3

class StreamChecker:

    def __init__(self, words):
        self.trie = {}
        for word in words:
            curr = self.trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['$'] = '$'
        self.ptrs = []

    def query(self, letter):
        self.ptrs = [ptr[letter] for ptr in self.ptrs + [self.trie] if letter in ptr]
        # print(f'checking {letter}')
        # print(f'{self.ptrs}')
        return any(['$' in ptr for ptr in self.ptrs])
        

words = ['cd', 'f', 'kl']
querys = list('abcdefghijkl')

sc = StreamChecker(words)
for q in querys:
    print(sc.query(q))
