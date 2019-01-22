#!/usr/bin/env python

class Solution:
    def removeInvalidParentheses(self, s, indent):
        """
        :type s: str
        :rtype: List[str]
        """
        ret, maxLen, prefix = [], 0, ''
        print(indent+'s = "%s"' % s)
        for i in range(len(s)):
            print(indent+'i = %d' % i)
            if s[i] == ')': continue
            elif s[i] != '(':
                prefix += s[i]
                continue
            for j in range(i+1, len(s)):
                print(indent+'j = %d' % j)
                if s[j] != ')': continue
                print(indent+'s[i+1:j-1] = "%s"' % s[i+1:j])
                print(indent+'s[j+1:] = "%s"' % s[j+1:])
                part1 = self.removeInvalidParentheses(s[i+1:j], indent+'  ')
                part2 = self.removeInvalidParentheses(s[j+1:], indent+'  ')
                print(indent+'part1 = "%s"' % (part1))
                print(indent+'part2 = "%s"' % (part2))
                for p in part1:
                    for q in part2:
                        valid = prefix+'('+p+')'+q
                        if len(valid) == maxLen and (valid not in ret):
                            ret.append(valid)
                        elif len(valid) > maxLen:
                            ret, maxLen = [valid], len(valid)
                            print(indent+'maxLen has been updated to = %d' % (maxLen))
                print(indent+'i = %d, j = %d, ret = %s' % (i, j, ret))
        ret = [prefix] if len(ret) == 0 else ret
        print(indent+'final ret for "%s" = %s' % (s, ret))
        return ret

s = '()'
s = ")("
s = ''
s = "(a)())()"
s = "()())()"
sol = Solution()
print(sol.removeInvalidParentheses(s, ''))
