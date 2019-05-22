#!/usr/bin/env python3

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = [[] for i in range(numCourses)]
        for p in prerequisites:
            edges[p[0]].append(p[1])
        print(edges)
        visited, stack = set(), set()
        self.feasible = True
        def dfs(p):
            visited.add(p)
            for q in edges[p]:
                if not self.feasible:
                    return
                if not q in visited:
                    dfs(q)
                elif not q in stack:
                    self.feasible = False
                    return
            stack.add(p)

        for p in range(numCourses):
            if not self.feasible:
                break
            if not p in visited:
                dfs(p)
        return self.feasible

numCourses, prerequisites = 2, [[1,0], [0,1]]
numCourses, prerequisites = 4, [[0,1],[1,2],[2,3],[3,0]]
numCourses, prerequisites = 4, [[0,1],[0,2],[1,3],[2,3]]
numCourses, prerequisites = 5, [[0,1],[1,2],[2,3],[3,0]]
numCourses, prerequisites = 2, [[1,0]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))

