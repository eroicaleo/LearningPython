#!/usr/bin/env python

import collections

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskDict, least, schedule = collections.defaultdict(int), 0, []
        for t in tasks:
            taskDict[t] += 1
        taskList = [[k, taskDict[k]] for k in taskDict]
        sortedTasks = sorted(taskList, key=lambda p: p[1], reverse=True)
        print(sortedTasks)
        while sortedTasks:
            i = n
            for t in sortedTasks:
                t[1], i, least = t[1]-1, i-1, least+1
                schedule.append(t[0])
                if i < 0:
                    break
            sortedTasks = list(filter(lambda p: p[1] > 0, sorted(taskList, key=lambda p: p[1], reverse=True)))
            if sortedTasks and n > 0:
                least += (i+1)
                schedule += [0] * (i+1)
            print(least, schedule, sortedTasks)
        return least
        # for t in sortedTasks:
        #     if not t in taskDict:
        #         continue
        #     else:
        #         m, l, emptyTask = taskDict[t], len(taskDict), []
        #         least += max(len(sortedTasks), n+1) * m
        #         for k in taskDict:
        #             # print(k, taskDict[k], taskDict[t])
        #             taskDict[k] -= m
        #             if taskDict[k] == 0:
        #                 emptyTask.append(k)
        #         [taskDict.pop(k) for k in emptyTask]
        #         if len(taskDict) == 0 and l < n+1:
        #             least -= (n+1-l)
        #             # print(k, taskDict[k])
        #     # print(t, taskDict, sortedTasks)
        # return least

sol = Solution()
tasks, n = list('AABB'), 1
tasks, n = list('AAAAAABCDEF'), 2
tasks, n = list('AAAABBBCC'), 2
print(sol.leastInterval(tasks, n))
