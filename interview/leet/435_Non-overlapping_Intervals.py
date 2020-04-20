#!/usr/bin/env python3

class Solution:
    def eraseOverlapIntervals(self, intervals):
        graph, l, edges = {}, len(intervals), 0
        for i in range(l):
            for j in range(i+1, l):
                e1, e2 = intervals[i], intervals[j]
                if max(e1[0], e2[0]) < min(e1[1], e2[1]):
                    graph.setdefault(i, set()).add(j)
                    graph.setdefault(j, set()).add(i)
                    edges += 1
        for k in sorted(graph):
            print(f'{k}: {graph[k]}')
        ret = 0
        while edges > 0:
            v, ret = max(graph, key=lambda v: len(graph[v])), ret+1
            for w in graph[v]:
                graph[w].remove(v)
                edges -= 1
            del graph[v]
        for k in sorted(graph):
            print(f'{k}: {graph[k]}')
        return ret

    def eraseOverlapIntervals_greedy(self, intervals):
        now = i = 0
        for v in sorted(intervals, key=lambda inter: inter[1]):
            if v[0] >= now:
                print(v)
                i, now = i+1, v[1]
        return i

sol = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
print(sol.eraseOverlapIntervals_greedy(intervals))

