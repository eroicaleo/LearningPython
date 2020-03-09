#!/usr/bin/env python3

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        edges = [list() for n in range(numCourses)]
        for p in prerequisites:
            edges[p[0]].append(p[1])
        print(edges)
        visited, done, sched = set(), set(), list()
        self.feasible = True
        def dfs(p):
            print(f'p={p}, visited={visited}, done={done}')
            if not self.feasible:
                return
            if p in visited:
                if not p in done:
                    self.feasible = False
                return
            visited.add(p)
            for q in edges[p]:
                dfs(q)
            done.add(p)
            sched.append(p)
        for p in range(numCourses):
            dfs(p)
        return sched if self.feasible else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 2
prerequisites = [[1,0]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))
