#!/usr/bin/env python3

class Solution(object):
    def insert(self, intervals, newInterval):
        # if not intervals:
        #     return [newInterval]
        lb, ub = newInterval
        ret, foundInsert, n = [], False, 0
        for n, i in enumerate(intervals+[[newInterval[1]+1, newInterval[1]+2]]):
            if not ((i[1] < newInterval[0]) or (newInterval[1] < i[0])):
                lb = min(lb, i[0])
                ub = max(ub, i[1])
                foundInsert = True
                print(lb, ub)
            elif (newInterval[1] < i[0]) or foundInsert:
                ret.append([lb,ub])
                break
            else:
                ret.append(i)
        return ret+intervals[n:]

intervals, newInterval = [[1,3],[6,9]], [2,5]
intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
intervals, newInterval = [[1,5]], [2,3]
intervals, newInterval = [[1,5]], [2,7]
intervals, newInterval = [], [2,5]
intervals, newInterval = [[1,3],[6,9]], [4,5]

sol = Solution()
print(sol.insert(intervals, newInterval))
