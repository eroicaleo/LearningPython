#!/usr/bin/env python

class Solution:
    def getSkyline(self, buildings):
        from heapq import heapify, heappush, heappop
        heaped, heaphi, ret, currhi = [], [0], [], 0
        for i, b in enumerate(buildings):
            while heaped and heaped[0][0] <= b[0]:
                ed, j = heappop(heaped)
                hi = buildings[j][2]
                index = heaphi.index(-hi)
                heaphi = heaphi[:index] + heaphi[index+1:]
                heapify(heaphi)
                if heaphi[0] > currhi: 
                    currhi = heaphi[0]
                    ret.append([ed, -currhi])
                    # print('currhi after pop:', ed, currhi)
                print("after pop heaphi:", heaphi)
            heappush(heaped, (b[1], i))
            heappush(heaphi, -b[2])
            print("after push heaphi:", heaphi)
            if heaphi[0] < currhi:
                currhi = heaphi[0]
                ret.append([b[0], -currhi])
                # print('currhi after push:', b[0], currhi)
        while heaped:
            ed, j = heappop(heaped)
            hi = buildings[j][2]
            index = heaphi.index(-hi)
            heaphi = heaphi[:index] + heaphi[index+1:]
            heapify(heaphi)
            if heaphi[0] > currhi: 
                currhi = heaphi[0]
                ret.append([ed, -currhi])
        return ret

buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
sol = Solution()
print(sol.getSkyline(buildings))
# print(list(range(5)).index(4))
