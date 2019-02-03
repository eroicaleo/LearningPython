#!/usr/bin/env python

import collections

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskDict = [0] * 26
        for t in tasks:
            taskDict[ord(t)-ord('A')] += 1
        taskDict = sorted(taskDict, reverse = True)
        k = 1
        while taskDict[k] == taskDict[0]:
            k += 1
        return max(len(tasks), (n+1)*(taskDict[0]-1)+k )

sol = Solution()
tasks, n = list('AABB'), 1
tasks, n = list('AAAAAABCDEF'), 2
tasks, n = list('AAAABBBCC'), 2
print(sol.leastInterval(tasks, n))
