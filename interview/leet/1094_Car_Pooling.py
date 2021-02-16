#!/usr/bin/env python3

from heapq import heappush, heappop
class Solution:
    def carPooling(self, trips, capacity):
        heap = []
        for n, s, e in trips:
            heappush(heap, (s, n))
            heappush(heap, (e, -n))
        while heap:
            # t, d = 
            capacity -= heappop(heap)[1]
            # print(f't = {t}, d = {d}, capacity = {capacity}')
            if capacity < 0:
                return False
        return True

sol = Solution()
trips, capacity = [[2,1,5],[3,3,7]], 5
trips, capacity = [[2,1,5],[3,5,7]], 3
trips, capacity = [[2,1,5],[3,3,7]], 4
trips, capacity = [[3,2,7],[3,7,9],[8,3,9]], 11

print(sol.carPooling(trips, capacity))
