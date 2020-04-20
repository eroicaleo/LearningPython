#!/usr/bin/env python3

import re

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution:
    def decodeString(self, s):
        stack, n, t = [], 0, ''
        for c in s:
            if c.isdigit():
                n = 10*n + int(c)
                if t:
                    stack, t = stack + [t], ''
            elif c == '[':
                stack.append(n)
                n, t = 0, ''
            elif c.isalpha():
                t += c
            elif c == ']':
                t = stack.pop() * t
                if stack and isinstance(stack[-1], str):
                    t = stack.pop() + t
            print(f'c = {c}, t = {t}, stack = {stack}')
        return t

    def decodeString_stefan(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]+)\]', lambda m: int(m.group(1)) * m.group(2), s)
            print(s)
        return s

    def decodeString_recursive(self, s):
        self.i, l = 0, len(s)
        def helper():
            n, t = 0, ''
            while self.i < l:
                c, self.i = s[self.i], self.i+1
                if c.isdigit():
                    n = 10*n+int(c)
                elif c.isalpha():
                    t += c
                elif c == '[':
                    t += n*helper()
                    n = 0
                elif c == ']':
                    break
            print(f'I am returning {t}')
            return t
        return helper()

    def decodeString_iter2(self, s):
        stack = []
        n, t = 0, ''
        for c in s:
            if c.isdigit():
                n = 10*n+int(c)
            elif c.isalpha():
                t += c
            elif c == '[':
                stack += [n, t]
                n, t = 0, ''
            elif c == ']':
                t, n = stack.pop()+stack.pop()*t, 0
        return t

s = "2[abc]3[cd]ef"
s = "3[3[a]3[b]]"
s = "3[a]2[bc]"
s = "3[a2[c]]"
sol = Solution()
print(sol.decodeString(s))
print('Solution 2')
print(sol.decodeString_stefan(s))
print('Solution 3')
print(sol.decodeString_recursive(s))
print('Solution 4')
print(sol.decodeString_iter2(s))
