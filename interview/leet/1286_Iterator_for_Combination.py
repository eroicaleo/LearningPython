#!/usr/bin/env python3

class CombinationIterator:
    def __init__(self, characters, combinationLength):
        self.ret, l = [], len(characters)
        def dfs(path, i):
            if len(path) == combinationLength:
                self.ret.append(path)
                return
            for j in range(i, l-(combinationLength-len(path))+1):
                dfs(path+characters[j], j+1)
        dfs('', 0)
        self.iter = 0

    def next(self):
        ele = self.ret[self.iter]
        self.iter += 1
        return ele

    def hasNext(self):
        return self.iter < len(self.ret)

comb = CombinationIterator('abcd', 5)
while comb.hasNext():
    print(comb.next())
