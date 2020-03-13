#!/usr/bin/env python

#       ----       ----------   
#       |  |       |        |
#       |  ---     |-----   |
#       |    |     |    |   |
#       |    |     |    |   |
# ---------------------------


from heapq import heapify, heappush, heappop
import math

class Solution:
    def getSkyline(self, buildings):
        heap, ret = [[0, -math.inf]], []
        for (li, ri, hi) in buildings + [[math.inf, math.inf, 0]]:
            print(f'li = {li}, ri = {ri}, hi = {hi}')
            while heap and -heap[0][1] < li:
                ri_top = -heappop(heap)[1]
                while heap and -heap[0][1] <= ri_top:
                    heappop(heap)
                ret.append([ri_top, -heap[0][0]])
            if ret and ret[-1][0] == li:
                ret[-1][1] = max(ret[-1][1], hi)
            elif hi > -heap[0][0]:
                ret.append([li, hi])
            heappush(heap, [-hi, -ri])
            print(f'heap = {heap}')
            print(f'ret = {ret}')

    def getSkyline_named_tuple(self, buildings):
        from collections import namedtuple
        building_info = namedtuple('building_info', ['neg_hi', 'neg_ri'])
        heap, ret = [building_info(0, -math.inf)], []
        for (li, ri, hi) in buildings + [[math.inf, math.inf, 0]]:
            while -heap[0].neg_ri < li:
                ri_top = -heappop(heap).neg_ri
                while -heap[0].neg_ri <= ri_top:
                    heappop(heap)
                ret.append([ri_top, -heap[0].neg_hi])
            if ret and ret[-1][0] == li:
                ret[-1][1] = max(ret[-1][1], hi)
            elif hi > -heap[0].neg_hi:
                ret.append([li, hi])
            heappush(heap, building_info(-hi, -ri))
        return ret


sol = Solution()
buildings_list = [
    [],
    [ [2, 3, 20],  [2, 4, 15], [2, 5, 10] ],
    [ [2, 3, 10],  [3, 4, 10], [4, 5, 10] ],
    [ [2, 3, 10],  [2, 4, 15], [2, 5, 20] ],
    [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ],
]
for buildings in buildings_list:
    print(f'buildings = {buildings}')
    print(sol.getSkyline_named_tuple(buildings))

