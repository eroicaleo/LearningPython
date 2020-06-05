#!/usr/bin/env python3

import itertools

class BIT:
    def __init__(self, f):
        self.f = f
        self.c = list(itertools.accumulate(f))
        print(self.c)
        self.MaxIdx = len(self.f)-1
        self.tree = [0]
        for idx in range(1, len(self.f)):
            r = idx - (idx & -idx) + 1
            self.tree.append(sum(self.f[r:idx+1]))
        print(self.tree)

    def read(self, idx):
        s = 0
        while idx:
            s += self.tree[idx]
            idx -= (idx & -idx)
        return s

    def update(self, idx, val):
        while idx <= self.MaxIdx:
            self.tree[idx] += val
            idx += (idx & -idx)

    def readSingle(self, idx):
        s = self.tree[idx]
        if idx > 0:
            z = idx - (idx & -idx)
            idx -= 1
            while idx != z:
                s -= self.tree[idx]
                idx -= (idx & -idx)
        return s

    def scale(self, c):
        for i in range(self.MaxIdx+1):
            self.tree[i] /= c
            self.f[i] /= c
        self.c = list(itertools.accumulate(f))

    def find(self, cumFre):
        idx, bitMask = 0, 1
        while bitMask <= self.MaxIdx:
            bitMask <<= 1
        bitMask >>= 1

        while bitMask > 0:
            tIdx = idx + bitMask
            bitMask >>= 1
            if tIdx > MaxIdx:
                continue
            if cumFre == self.tree[tIdx]:
                return tIdx
            elif cumFre > tree[tIdx]:
                idx = tIdx
                cumFre -= tree[tIdx]
        return idx if cumFre == 0 else -1

if __name__ == '__main__':

    f = [0,1,0,2,1,1,3,0,4,2,5,2,2,3,1,0,2]
    bit = BIT(f)
    for idx, s in enumerate(bit.c):
        print(f'{s}, {bit.read(idx)}')
    print('#'*80)
    print('check update')
    print('#'*80)
    print(f'{bit.tree}')
    bit.update(5, -1)
    print(f'{bit.tree}')
    bit.update(5, +1)
    print(f'{bit.tree}')
    print('#'*80)
    print('check readSingle')
    print('#'*80)
    for idx, s in enumerate(bit.f):
        print(f'{s}, {bit.readSingle(idx)}')

    print('#'*80)
    print('check scale')
    print('#'*80)
    bit.scale(2.0)
    for idx, s in enumerate(bit.f):
        print(f'{s}, {bit.readSingle(idx)}')
    bit.scale(0.5)
    for idx, s in enumerate(bit.f):
        print(f'{s}, {bit.readSingle(idx)}')
