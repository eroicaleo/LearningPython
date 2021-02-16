#!/usr/bin/env python3

class Solution:
    def partition(self, s):
        def isPad(s):
            return s == s[::-1]
        l = len(s)
        pt = [[0]*l for _ in range(l)]
        for i in range(l):
            for j in range(i+1,l+1):
                if isPad(s[i:j]):
                    pt[i][j-1] = 1
        # print(f'pt = {pt}')
        self.ret = []
        def dfs(pre, k):
            if k == l:
                self.ret.append(pre)
                return
            for i in range(k,l):
                if pt[k][i] == 1:
                    dfs(pre+[s[k:i+1]], i+1)
        dfs([], 0)
        return self.ret

    # ϕ a a b
    def partition_fastest(self, s):
        def isPad(s):
            return s == s[::-1]
        dp, l = [[[]]], len(s)
        for i in range(l):
            dp.append([])
            for j in range(0, i+1):
                if isPad(s[j:i+1]):
                    for t in dp[j]:
                        dp[-1].append(t+[s[j:i+1]])
            print(dp)
        return dp[-1]


s = 'aab'
s = 'a'
s = ''
sol = Solution()
print(sol.partition_fastest(s))

