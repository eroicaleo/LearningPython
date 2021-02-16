#!/usr/bin/env python3

from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times, N, K):
        graph, heap, dist = {}, [(0, K)], [0]+[float('inf')]*N
        res = 0
        for s, e, w in times:
            graph.setdefault(s, []).append((e, w))
        while heap:
            d, K = heappop(heap)
            if d < dist[K]:
                res, dist[K], N = d, d, N-1
                for e, w in graph.setdefault(K, []):
                    d = dist[K] + w
                    if d < dist[e]:
                        heappush(heap, (d, e))
            # print(f'dist = {dist}, heap = {heap}, N = {N}')
        return -1 if N > 0 else res

    def networkDelayTime_Bellman_Ford(self, times, N, K):
        dist = [0]+[float('inf')]*N
        dist[K] = 0
        for _ in range(N):
            for u, v, w in times:
                if dist[u] != float('inf') and dist[v]>dist[u]+w:
                    dist[v] = dist[u]+w
        ret = 0
        for d in dist:
            if d == float('inf'):
                return -1
            ret = max(d, ret)
        return ret

times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
sol = Solution()
print(sol.networkDelayTime(times, N, K))
print(sol.networkDelayTime_Bellman_Ford(times, N, K))
