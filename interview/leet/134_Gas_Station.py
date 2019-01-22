#!/usr/bin/env python

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length, start = len(gas), 0
        diff = [0] * length
        for i in range(length):
            diff[i] = gas[i] - cost[i]
        for start in range(length):
            gasLeft = 0
            for i in range(length):
                gasLeft += diff[(start+i)%length]
                if gasLeft < 0: break
            else: return start
        return -1


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
gas  = [2,3,4]
cost = [3,4,3]
gas  = []
cost = []
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
