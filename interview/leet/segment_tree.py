#!/usr/bin/env python3

# If there are n elements in the array
# How many poins in the tree?
# It's full binary tree and it has n leave nodes
# So it has 2n-1 nodes. This can be proved using induction
# So if we include dummy nodes, it is going to be 2 * (2^x)-1
# x = math.ceil(math.log2(n))
# For example: when n = 10, x = 4, there are 31 nodes in total

import math

class segment_tree:
    def __init__(self, a):
        self.length = len(a)
        x = math.ceil(math.log2(self.length))
        self.tree = [None]*(1<<(x+1)) # We use 1-based index
        self.lazy = [0]*(1<<(x+1))
        print(f'x = {x}, length of tree is {len(self.tree)}')
        def helper(node, l, r):
            if l == r:
                self.tree[node] = a[l]
            else:
                m = (l+r)//2
                self.tree[node] = helper(2*node, l, m) + helper(2*node+1, m+1, r)
            return self.tree[node]
        helper(1, 0, self.length-1)
        print(f'tree after preprocessing {self.tree}')
        assert self.check(a)

    def check(self, a):
        for i in range(len(a)):
            for j in range(i, len(a)):
                q, s = self.query(i, j), sum(a[i:j+1])
                if  q != s:
                    return False
        return True

    def check_query_lazy(self, a):
        for i in range(len(a)):
            for j in range(i, len(a)):
                # print(f'check_query_lazy: i = {i}, j = {j}')
                q, s = self.query_range_lazy(i, j), sum(a[i:j+1])
                # print(f'tree after query_range_lazy {self.tree}')
                # print(f'lazy after query_range_lazy {self.lazy}')
                if  q != s:
                    print(f'self.query_range_lazy(i, j) = {q}, sum(a[i:j+1]) = {s}')
                    return False
        return True

    def update(self, i, n):
        def helper(i, n, node, l, r):
            print(f'Going in helper node = {node}, l = {l}, r = {r}')
            if l == r:
                self.tree[node] = n
                return
            m = (l+r)//2
            if i <= m:
                helper(i, n, 2*node, l, m)
            else:
                helper(i, n, 2*node+1, m+1, r)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        helper(i, n, 1, 0, self.length-1)
        print(f'tree after update {self.tree}')

    def query(self, s, e):
        def helper(node, s, e, l, r):
            # print(f'Going in query helper node = {node}, s = {s}, e = {e}, l = {l}, r = {r}')
            if s <= l and r <= e:
                return self.tree[node]
            if e < l or s > r:
                return 0
            m = (l+r)//2
            return helper(2*node, s, e, l, m) + helper(2*node+1, s, e, m+1, r)
        return helper(1, s, e, 0, self.length-1)

    # lazy version
    def update_range_lazy(self, s, e, val):
        def update_range_lazy_helper(node, s, e, l, r, val):
            if e < l or s > r:
                return

            # condition 1: has pending update, make the child nodes lazy
            if self.lazy[node] != 0:
                self.tree[node] += (r-l+1)*self.lazy[node]
                if l < r:
                    self.lazy[2*node] += self.lazy[node]
                    self.lazy[2*node+1] += self.lazy[node]
                self.lazy[node] = 0

            # condition 2: segment lays completely in [s, e]
            if s <= l and r <= e:
                self.tree[node] += (r-l+1)*val
                if l < r:
                    self.lazy[2*node] += val
                    self.lazy[2*node+1] += val
                return

            # condition 3: [l,r] intersects with [s,e]
            m = (l+r)//2
            update_range_lazy_helper(2*node,   s, e, l,   m, val)
            update_range_lazy_helper(2*node+1, s, e, m+1, r, val)
            self.tree[node] = self.tree[2*node]+self.tree[2*node+1]
            return
        update_range_lazy_helper(1, s, e, 0, self.length-1, val)
        print(f'tree after update_range_lazy {self.tree}')
        print(f'lazy after update_range_lazy {self.lazy}')

    def query_range_lazy(self, s, e):
        def query_range_lazy_helper(node, s, e, l, r):
            # print(f'Going in query_range_lazy_helper node = {node}, s = {s}, e = {e}, l = {l}, r = {r}')
            if e < l or s > r:
                return 0

            if self.lazy[node] != 0:
                self.tree[node] += (r-l+1)*self.lazy[node]
                if l < r:
                    self.lazy[2*node] += self.lazy[node]
                    self.lazy[2*node+1] += self.lazy[node]
                self.lazy[node] = 0
            # print(f'tree after query_range_lazy_helper {self.tree}')
            # print(f'lazy after query_range_lazy_helper {self.lazy}')

            if s <= l and r <= e:
                return self.tree[node]

            m = (l+r)//2
            q_l = query_range_lazy_helper(2*node,   s, e, l,   m)
            q_r = query_range_lazy_helper(2*node+1, s, e, m+1, r)
            return q_l+q_r
        return query_range_lazy_helper(1, s, e, 0, self.length-1)
            

if __name__ == '__main__':

    a = [1, 3, 5, 7, 9, 11]
    print(f'a = {a}')
    st = segment_tree(a)

    # st.update(1, 10)
    s, e = 0, 1
    print(f'query between [{s}, {e}]: {st.query(s, e)}')

    for s in range(len(a)):
        for e in range(s, len(a)):
            print(f'update a by adding 1 [{s}, {e}]')
            a = a[:s]+[i+1 for i in a[s:e+1]]+a[e+1:]
            print(f'a = {a}')
            st.update_range_lazy(s, e, 1)
            assert st.check_query_lazy(a)
            print(f'tree after check_query_lazy {st.tree}')
            print(f'lazy after check_query_lazy {st.lazy}')
