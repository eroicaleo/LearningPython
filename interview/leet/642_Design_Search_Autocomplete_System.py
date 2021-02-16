#!/usr/bin/env python

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = {}
        for sentence, n in zip(sentences, times):
            d = self.trie
            for c in sentence:
                d = d.setdefault(c, {})
            d['#'] = (-n, sentence)

        self.curr = self.trie
        self.pfix = ''

    def dfs(self, d):
        if '#' in d:
            self.res.append(d['#'])
        [self.dfs(d[c]) for c in d if c != '#']

    def input(self, c):
        if c == '#':
            self.curr['#'] = (self.curr.get('#', (0,''))[0]-1, self.pfix)
            self.curr = self.trie
            self.pfix = ''
            return []
        self.res = []
        self.dfs(self.curr.setdefault(c, {}))
        self.pfix += c
        self.curr = self.curr[c]
        return [s for n, s in sorted(self.res)[:3]]

sentences = [
    "i love you",
    "island",
    "ironman",
    "i love leetcode",
]

times = [5,3,2,2]

obj = AutocompleteSystem(sentences, times)
for _ in range(6):
    for c in 'i a#':
        print(f'curr = {obj.curr}\n', f'prefix = "{obj.pfix}"\n', f'return = {obj.input(c)}')
        print('#'*80)
