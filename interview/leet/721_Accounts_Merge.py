#!/usr/bin/env python

class Solution:
    def accountsMerge(self, accounts):
        union, name, bag = {}, {}, {}
        for acc in accounts:
            for e in acc[1:]:
                if e not in union:
                    union.setdefault(e, acc[1])
                    bag.setdefault(union[e], set()).add(e)
            name.setdefault(union[acc[1]], acc[0])
            p = acc[1]
            for q in acc[1:]:
                rootp, rootq = union[p], union[q]
                if rootp == rootq:
                    continue
                if len(bag[rootp]) < len(bag[rootq]):
                    rootp, rootq = rootq, rootp
                for e in bag[rootq]:
                    union[e] = rootp
                bag[rootp] = bag[rootp].union(bag[rootq])
                del bag[rootq], name[rootq]
            print('After union')
            print(f'name = {name}\nunion = {union}\nbag = {bag}')
        return [[name[k], *sorted(bag[k])] for k in name]

accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]
]

accounts = [
        ['Peppa', 'p0', 'p1', 'p2', 'p3'],
        ['Peppa', 'g0', 'g1', 'g2', 'g3'],
        ['Peppa', 'm0', 'm1', 'm2', 'm3'],
        ['Peppa', 'd0', 'p1', 'g2', 'm3'],
]

accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "john_newyork@mail.com", "johnsmith@mail.com" ], 
        ["John", "john00@mail.com", "john_newyork@mail.com" ], 
        ["Mary", "mary@mail.com"]
]

bag, union = {}, {}
# bag.setdefault('k', set()).add('a')
union.setdefault('k', 'k')
bag.setdefault(union['k'], set()).add('k')
print(union)
print(bag)
sol = Solution()
print(sol.accountsMerge(accounts))


