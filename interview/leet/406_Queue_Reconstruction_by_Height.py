#!/usr/bin/env python

class Solution:
    def reconstructQueue(self, people):
        queue = []
        for p in sorted(people, key=lambda p: [p[1], p[0]]):
            h, k, i = p[0], p[1], 0
            for j in range(len(queue)):
                if h <= queue[j][0]:
                    i += 1
                if i > k:
                    queue.insert(j, p)
                    break
            else:
                queue.append(p)
            print(f'h={h}, k={k}, queue={queue}')
        return queue

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

sol = Solution()
print(sol.reconstructQueue(people))
