#!/usr/bin/env python

class Solution:
    def leastInterval(self, tasks, n):

sol = Solution()
tasks, n = list('AABB'), 1
tasks, n = list('AAAAAABCDEF'), 2
tasks, n = list('AAAABBBCC'), 2
print(sol.leastInterval(tasks, n))
