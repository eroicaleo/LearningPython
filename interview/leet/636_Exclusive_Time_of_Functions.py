#!/usr/bin/env python3

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        from collections import deque
        timeTable = [0] * n
        stack = deque()
        currentTime = 0
        for task in logs:
            taskID, state, timestamp = task.split(':')
            taskID, timestamp = int(taskID), int(timestamp)
            if state == 'start':
                if stack:
                    stack[-1][2] += (timestamp-stack[-1][1])
                stack.append([taskID, timestamp, 0])
            else:
                timeTable[stack[-1][0]] += (timestamp-stack[-1][1]+1) + stack[-1][2]
                stack.pop()
                if stack:
                    stack[-1][1] = timestamp+1
            # print(timeTable)
        return [t for t in timeTable if t > 0]

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
sol = Solution()
print(sol.exclusiveTime(n, logs))
