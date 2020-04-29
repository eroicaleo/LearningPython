#!/usr/bin/env python3

class IndexMinPQ:
    def __init__(self, maxN):
        if maxN < 0:
            raise ValueError(f'IndexMinPQ can not be initialized with negative ({maxN}) size')
        self.maxN = maxN
        self.n = 0
        self.pq = [-1]*(1+maxN) # pq[i] the index on heap position i
        self.qp = [-1]*(1+maxN) # qp[i] the heap position of index i qp[pq[i]] = pq[qp[i]] = i
        self.keys = [None]*(1+maxN) # keys[i] = priority of index i

    def isEmpty(self):
        return self.n == 0

    def contains(self, i):
        self.validateIndex(i)
        return self.qp[i] != -1

    def validateIndex(self, i):
        if not (0 <= i < self.maxN):
            raise ValueError(f'index ({i}) has to be between [0, {self.maxN-1})')

    def size(self):
        return self.n

    def insert(self, i, key):
        self.validateIndex(i)
        if self.contains(i):
            raise ValueError(f'index ({i}) is already in the priority queue')
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)

    def swim(self, k):
        while k > 1 and self.greater(k//2, k):
            self.exch(k, k//2)
            k //= 2

    def sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self.greater(j, j+1):
                j += 1
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        v, w = self.pq[i], self.pq[j]
        self.pq[i], self.pq[j], self.qp[v], self.qp[w] = w, v, j, i

    def minIndex(self):
        if self.n == 0:
            raise IndexError('priority queue underflow in minIndex!')
        return self.pq[1]

    def minKey(self):
        if self.n == 0:
            raise IndexError('priority queue underflow in minKey!')
        return self.keys[self.pq[1]]

    def delMin(self):
        if self.n == 0:
            raise IndexError('priority queue underflow in delMin!')
        i = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        assert i == self.pq[self.n+1], 'The index {i}, key: {self.keys[i]} needs to be in pq[{self.n+1}]'
        self.qp[i] = -1
        self.keys[i] = None
        self.pq[self.n+1] = -1
        return i

    def keyOf(self, i):
        self.validateIndex(i)
        if not self.contains(i):
            raise ValueError(f'index ({i}) is not in the priority queue')
        return self.keys[i]

    def changeKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i):
            raise ValueError(f'index ({i}) is not in the priority queue')
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def decreaesKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i):
            raise ValueError(f'index ({i}) is not in the priority queue')
        if self.keys[i] == key:
            raise ValueError(f'index (self.keys[{i}] = {self.keys[i]}) equals to {key}')
        if self.keys[i] < key:
            raise ValueError(f'index (self.keys[{i}] = {self.keys[i]}) scrictly less than {key}')
        self.keys[i] = key
        self.swim(self.qp[i])

    def increaesKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i):
            raise ValueError(f'index ({i}) is not in the priority queue')
        if self.keys[i] == key:
            raise ValueError(f'index (self.keys[{i}] = {self.keys[i]}) equals to {key}')
        if self.keys[i] > key:
            raise ValueError(f'index (self.keys[{i}] = {self.keys[i]}) scrictly greater than {key}')
        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        self.validateIndex(i)
        if not self.contains(i):
            raise ValueError(f'index ({i}) is not in the priority queue')
        j = self.qp[i]
        self.exch(j, self.n)
        self.n -= 1
        self.sink(j)
        self.swim(j)
        assert i == self.pq[self.n+1], 'The index {i}, key: {self.keys[i]} needs to be in pq[{self.n+1}]'
        self.pq[self.n+1] = -1
        self.qp[i] = -1
        self.keys[i] = None

    def validateHeap(self):
        i = 1
        if any(self.pq[i] == -1 for i in range(1, self.n+1)):
            print(f'{self.pq} has -1')
            return False
        if any(self.pq[i] != -1 for i in range(self.n+1, self.maxN+1)):
            print(f'{self.pq} has non -1')
            return False
        while 2*i <= self.n:
            if self.greater(i, 2*i):
                print(f'heap[{i}] = {self.keys[self.pq[i]]} > heap[{2*i}] = {self.keys[self.pq[2*i]]}')
                return False
            if 2*i+1 <= self.n and self.greater(i, 2*i+1):
                print(f'heap[{i}] = {self.keys[self.pq[i]]} > heap[{2*i+1}] = {self.keys[self.pq[2*i+1]]}')
                return False
            i += 1
        return True

    def __str__(self):
        k = i = 1
        ret = ''
        while k <= self.n:
            for i in range(k, min(k*2, self.n+1)):
                ret += f'heap position {i}, index {self.pq[i]}, key "{self.keys[self.pq[i]]}" '
            ret += '\n'
            k *= 2
        return ret

if __name__ == '__main__':

    def print_banner(s):
        print('##------------------------------------------------------------------------------')
        print(f'## {s}')
        print('##------------------------------------------------------------------------------')
 
    try:
        IndexMinPQ(-1)
    except ValueError as err:
        print(f'got this error: {err}')

    strings = [ "it", "was", "the", "best", "of", "times", "it", "was", "the", "worst" ];
    pq = IndexMinPQ(len(strings))
    print(f'pq.isEmpty = {pq.isEmpty()}')

    print_banner('Test contains')
    try:
        pq.contains(-1)
    except ValueError as err:
        print(f'got this error: {err}')

    try:
        pq.contains(len(strings))
    except ValueError as err:
        print(f'got this error: {err}')

    print_banner('Test minIndex underflow')
    try:
        pq.minIndex()
    except IndexError as err:
        print(f'got this error: {err}')

    print_banner('Test minKey underflow')
    try:
        pq.minKey()
    except IndexError as err:
        print(f'got this error: {err}')

    print_banner('Test insert')
    for i, s in enumerate(strings):
        pq.insert(i, s)
        print(f'index ({i}), key "{pq.keyOf(i)}", minIndex: {pq.minIndex()}, minKey: {pq.minKey()}')

    print_banner('Test changeKey')
    pq.changeKey(9, 'alex')
    print(f'{pq}')
    pq.changeKey(9, 'worst')
    print(f'{pq}')

    print_banner('Test decreaesKey')
    try:
        pq.decreaesKey(9, 'worst')
    except ValueError as err:
        print(f'got this error: {err}')
    try:
        pq.decreaesKey(9, 'zebra')
    except ValueError as err:
        print(f'got this error: {err}')
    pq.decreaesKey(9, 'alex')
    print(f'{pq}')

    print_banner('Test increaesKey')
    try:
        pq.increaesKey(9, 'alex')
    except ValueError as err:
        print(f'got this error: {err}')
    try:
        pq.increaesKey(9, 'aha')
    except ValueError as err:
        print(f'got this error: {err}')
    pq.increaesKey(9, 'worst')
    print(f'{pq}')

    print_banner('Test delMin')
    while not pq.isEmpty():
        i = pq.delMin()
        print(f'index {i}, key {strings[i]}')

    print_banner('Re insert')
    for i, s in enumerate(strings):
        pq.insert(i, s)
        print(f'index ({i}), key "{pq.keyOf(i)}", minIndex: {pq.minIndex()}, minKey: {pq.minKey()}')

    print_banner('Test delete')
    import random
    s = list(range(len(strings)))
    random.shuffle(s)
    for i in s:
        print(f'delete index {i}')
        pq.delete(i)
        assert pq.validateHeap()
        print(pq)
