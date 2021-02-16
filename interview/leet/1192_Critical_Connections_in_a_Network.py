#!/usr/bin/env python

class Solution:
    def criticalConnections(self, n, connections):
        connections = set([(v, w) if v < w else (w, v) for v, w in connections])
        print(f'connections = {connections}')
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        rank, cycle = [-2]*n, set()

        def dfs(v, depth):
            rank[v] = min_back_depth = depth
            print(' '*2*depth + f'visiting {v}, depth = {depth}')
            for w in graph[v]:
                if rank[w] == depth-1:
                    continue
                back_depth = dfs(w, depth+1) if rank[w] < 0 else rank[w]
                if back_depth <= rank[v]:
                    cycle.add((v, w) if v < w else (w, v))
                min_back_depth = min(back_depth, min_back_depth)
            print(' '*2*depth + f'finishing {v}, min_back_depth = {min_back_depth}')
            return min_back_depth

        dfs(0, 0)
        return list(connections-cycle)


connections = [
    [0,1],
    [1,2],
    [2,0],
    [1,3],
]
sol = Solution()
print(sol.criticalConnections(4, connections))
