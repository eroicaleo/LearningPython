#!/usr/bin/env python3

# https://codeforces.com/blog/entry/18051
# This code use Increment as modifications
# And use queries for maximum

import math
import operator

class segment_tree:
    def __init__(self, a):
        self.n = len(a)
        self.tree = [0]*self.n + a
        self.lazy = [0]*self.n
        self.H = math.ceil(math.log2(self.n))
        print(f'self.tree before build: {self.tree}')
        self.build()
        print(f'self.tree after build: {self.tree}')

    def visualize_tree(self):
        width = 8
        x = math.ceil(math.log2(self.n))
        i = 1
        print('='*(2**x*width))
        while i <= (2**x):
            # print(f'visualize_tree, i = {i}')
            w = (2**x//i*width-1)
            for k in range(i):
                node = i+k
                v = self.tree[node] if node < len(self.tree) else 'x'
                s = f'{node}: {v}' + (f' ({self.lazy[node]})' if node < len(a) else '')
                print(f'{s:^{w}}|', end='')
            print()
            for k in range(i):
                print(f'{"_"*w+"|"}', end='')
            print()
            i *= 2

    def build(self):
        for i in range(self.n-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def modify(self, p, value):
        p += self.n
        self.tree[p] = value
        while p > 1:
            self.tree[p//2] = self.tree[p] + self.tree[p^1]
            p //= 2

    def query(self, l, r):
        res = 0
        l, r = l+self.n, r+self.n
        self.push(l); self.push(r)
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1 == 0: # Note here, we query [l, r]
                res = max(res, self.tree[r])
                r -= 1
            l, r = l//2, r//2
        return res

    def update(self, l, r, val):
        l, r = l+self.n, r+self.n
        l0, r0 = l, r
        while l <= r:
            if l & 1:
                res = self.apply(l, val)
                l += 1
            if r & 1 == 0: # Note here, we query [l, r]
                res = self.apply(r, val)
                r -= 1
            l, r = l//2, r//2
        print(f'update before pull(l0)'); self.visualize_tree()
        self.pull(l0)
        print(f'update after pull(l0) before pull(r0)'); self.visualize_tree()
        self.pull(r0)
        print(f'update after pull(r0)'); self.visualize_tree()

    def apply(self, node, value):
        print(f'apply node = {node}, value = {value}')
        self.tree[node] += value
        if node < self.n: # internal nodes
            self.lazy[node] += value

    def pull(self, node):
        while node > 1:
            node //= 2
            self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])
            self.tree[node] = self.tree[node] + self.lazy[node]

    def push(self, node):
        for h in range(self.H, 0, -1):
            y = node >> h
            if self.lazy[y]:
                self.apply(y*2,   self.lazy[y])
                self.apply(y*2+1, self.lazy[y])
                self.lazy[y] = 0

    def check(self):
        for i in range(self.n):
            for j in range(self.n):
                q, s = self.query(i, j), sum(self.tree[self.n+i:self.n+j+1])
                if  q != s:
                    print(f'i, j = {i}, {j}, self.query(i, j) = {q}, sum(a[i:j+1]) = {s}')
                    return False
        return True

if __name__ == '__main__':
    a = list(range(13))
    a = list(range(16))
    st = segment_tree(a)
    print('#'*80)
    print(f'Original tree')
    print('#'*80)
    st.visualize_tree()

    l, r, val = 2, 3, 1
    print('#'*80)
    print(f'update l = {l}, r = {r}, val = {val}')
    print('#'*80)
    st.update(l, r, val)

    # st.modify(0, 1)
    # print(f'After st.modify(0, 1), self.tree =')
    # st.visualize_tree()
    # st.modify(0, 0)
    # print(f'After st.modify(0, 0), self.tree =')
    # st.visualize_tree()
    # assert st.check()
    # l, r = 3, 10
    # print(f'After query({l}, {r}) = {st.query(l, r)}, tree = ')
    # st.visualize_tree()
    # st.update(l, r, 1)
    # print(f'After update({l}, {r}), tree = ')
    # st.visualize_tree()
    # print(f'After query({l}, {r}) = {st.query(l, r)}, tree = ')
    # st.visualize_tree()
