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
                    timeTable[stack[-1]] += timestamp - currentTime
                stack.append(taskID)
                currentTime = timestamp
            else:
                timeTable[stack[-1]] += timestamp - currentTime + 1
                stack.pop()
                currentTime = timestamp + 1
            # print(timeTable)
            # print(stack)
        return [t for t in timeTable if t > 0]

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
sol = Solution()
print(sol.exclusiveTime(n, logs))
