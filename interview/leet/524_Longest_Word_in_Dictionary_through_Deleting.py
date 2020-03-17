#!/usr/bin/env python

# Example 1:
# Input:s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:
# Input:s = "abpcplea", d = ["a","b","c"]
# Output: "a"

#   Ф a b p c p l e a
# Ф 1 0 0 0 0 0 0 0 0
# a 0 1 1 1 1 1 1 1 1
# p 0 0 0 1 1 1 1 1 1 
# p 0 0 0 0 0 1 1 1 1
# l 0 0 0 0 0 0 1 1 1
# e 0 0 0 0 0 0 0 1 1

class Solution:
    def findLongestWord(self, s, d):
        self.s_len = len(s)
        return min([self.dp(s, d_s) for d_s in d], key=lambda x: (-len(x), x))

    def dp(self, s, d_s):
        self.curr_row, self.last_row = [0]+[0]*self.s_len, [1]+[1]*self.s_len
        print(s, d_s)
        for c in d_s:
            for i in range(1, self.s_len+1):
                self.curr_row[i] = max(self.curr_row[i-1], int(self.last_row[i-1] and (c == s[i-1])))
            self.curr_row, self.last_row = [0]+[0]*self.s_len, self.curr_row
            print(self.last_row)
        return ['', d_s][self.last_row[-1]]

sol = Solution()
s = "abpcplea"
d = ['a', 'b', 'c']
s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(sol.findLongestWord(s, d))
