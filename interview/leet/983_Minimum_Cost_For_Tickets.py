#!/usr/bin/env python3

# Thinking process:

# This doesn't work
# We need 3 DP tables:
# TD: at day i, if we have a 1-day pass, the [min cost, days left]
# TW: at day i, if we have a 1-week pass, the [min cost, days left]
# TM: at day i, if we have a 1-month pass, the [min cost, days left]

# Recurrence relation
# TD[i] = min(TD[i-1].mincost, TW[i-1].mincost, TM[i-1].mincost) + cost[0]
# TW[i] = TW[i-1] if TW[i-1].daysleft > 1 else min(TD[i-1].mincost, TW[i-1].mincost, TM[i-1].mincost) + cost[1]
# TM[i] = TM[i-1] if TM[i-1].daysleft > 1 else min(TD[i-1].mincost, TW[i-1].mincost, TM[i-1].mincost) + cost[2]

class Solution:
    def mincostTickets(self, days, costs):
        cd, cw, cm = costs
        ld, lw, lm = 1, 7, 30
        for d in range(days[0]+1, days[-1]+1):
            ld, lw, lm = ld-1, lw-1, lm-1
            if d in days:
                m = min(cd, cw, cm)
                cd, ld = m + costs[0], 1
                if lw <= 0:
                    cw, lw = m + costs[1], 7
                if lm <= 0:
                    cm, lm = m + costs[2], 30
            print(f'd = {d}, ({cd}, {ld}), ({cw}, {lw}), ({cm}, {lm})')

    def mincostTickets_2(self, days, costs):
        cd, cw, cm = costs
        ld, lw, lm = 1, 7, 30
        for i in range(1, len(days)):
            diff = days[i]-days[i-1]
            ld, lw, lm = ld-diff, lw-diff, lm-diff
            m = min(cd, cw, cm)
            cd, ld = m + costs[0], 1
            if lw <= 0:
                cw, lw = m + costs[1], 7
            if lm <= 0:
                cm, lm = m + costs[2], 30
            print(f'd = {days[i]}, ({cd}, {ld}), ({cw}, {lw}), ({cm}, {lm})')
        return min(cd, cw, cm)

    def mincostTickets_3(self, days, costs):
        dp = [0]*(days[-1]+1)
        for i in range(days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i]=min(dp[max(0,i-7)]+costs[1],dp[max(0,i-1)]+costs[0],dp[max(0,i-30)]+costs[2])
            print(f'd = {i}, dp[i] = {dp[i]}')
        return dp[-1]

    def mincostTickets_noDP(self, days, costs):
        l = len(days)
        ret, ix, cost = [float('inf')]*l, [0,0], 0
        for i, d in enumerate(days):
            ret[i] = min(ret[i], cost+costs[0])
            for j in range(ix[0], l):
                if days[j] >= d+7:
                    ix[0] = j
                    break
                ret[j] = min(ret[j], cost+costs[1])
            for j in range(ix[1], l):
                if days[j] >= d+30:
                    ix[1] = j
                    break
                ret[j] = min(ret[j], cost+costs[2])
            cost = ret[i]
            print(f'{d}: {ret}')
        return ret[-1]

days = [1,4,6,7,8,20]
costs = [7,2,15]
days = [4,5,9,11,14,16,17,19,21,22,24]
costs = [1,4,18]
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
days = [1,4,6,7,8,20]
costs = [2,7,15]

sol = Solution()
print(sol.mincostTickets_2(days, costs))
print(sol.mincostTickets_3(days, costs))
print(sol.mincostTickets_noDP(days, costs))
