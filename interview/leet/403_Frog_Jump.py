#!/usr/bin/env python3

class Solution:
    def canCross(self, stones) -> bool:
        visited = {}
        def dfs(node):
            print('I am visiting: ', node)
            visited[node], stone, step = 1, node[0], node[1]
            if stone == stones[-1]:
                return True
            for s in range(max(1,step-1), step+2):
                next_node, next_stone = (stone+s, s), stone+s
                if (next_stone in stones) and (next_node not in visited):
                    if dfs(next_node):
                        return True
            return False
        return dfs((0, 0))

sol = Solution()
stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]
print(sol.canCross(stones))
