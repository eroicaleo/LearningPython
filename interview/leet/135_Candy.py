#!/usr/bin/env python

class Solution:
    def candy(self, ratings):
        l, ratings_sorted = len(ratings), sorted([(r, i) for i, r in enumerate(ratings)])
        candy_list = [1]*l
        for r, ix in ratings_sorted:
            candy_list[ix] = 1
            if ix > 0 and ratings[ix-1] < ratings[ix]:
                candy_list[ix] = max(candy_list[ix], candy_list[ix-1]+1)
            if ix < l-1 and ratings[ix+1] < ratings[ix]:
                candy_list[ix] = max(candy_list[ix], candy_list[ix+1]+1)
        print(f'candy_list = {candy_list}')
        return sum(candy_list)

ratings = [1,2,2]
ratings = [1,0,2]
sol = Solution()
print(sol.candy(ratings))
