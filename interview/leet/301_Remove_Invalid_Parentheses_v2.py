#!/usr/bin/env python

# This is the copy of highest voted solution in discussion
# Some properties: if it's a valid one, from left to right, the number of '(' should be
# greater or equal to # of ')', if we see ')' is more than '(', we know
# we need to remove one of ')' to make it valid
# If we convert them to an array, increaase by 1 if sees '('
# decrease by 1 if sees ')', then whenever we see positive number, we know
# we need to remove 1 ')'
# For example, s = "()())()"
# the array would be [1, 0, 1, 0, -1, 0, -1]
# At position 4, we see the -1, then we can choose the ')' in
# position 1 or 3 to remove.

# proposition 1 (uniqueness of the following algorithm):
# Assuming ')' is more than '(', this algorithm always remove from the first
# of consecutive '('s, then if removed place is different, than resulted valid string
# is different
# if '...)(+)...'

# proposition 2 (completeness): 

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        self.remove(s, ret, 0, 0, ['(', ')'])
        return ret

    def remove(self, s, ans, last_i, last_j, par):
        stack = 0
        # print(indent+'s = "%s", last_i = %d, last_j = %d' % (s, last_i, last_j))
        for i in range(last_i, len(s)):
            # print(indent+'i = %d, s = "%s", s[i] = "%s"' % (i, s, s[i]))
            if s[i] == par[0]: stack += 1
            if s[i] == par[1]: stack -= 1
            if stack >= 0: continue
            for j in range(last_j, i+1):
                # print(indent+'j = %d, s = "%s", s[j] = "%s"' % (j, s, s[j]))
                if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                    self.remove(s[:j]+s[j+1:], ans, i, j, par)
            return
        reverse = s[::-1]
        if par[0] == '(':
            self.remove(reverse, ans, 0, 0, list(')('))
        else:
            ans.append(reverse)

s = "()())()"
s = "()()))))()"
s = "(a)())()"
sol = Solution()
print(sol.removeInvalidParentheses(s))
