#!/usr/bin/env python3

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        from collections import deque
        stack = deque()
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                op1 = stack.pop()
                op2 = stack.pop()
                if   c == '+': res = op2 +  op1
                elif c == '-': res = op2 -  op1
                elif c == '*': res = op2 *  op1
                elif c == '/':
                    if (op2 < 0 and op1 > 0) or ((op1 < 0) and (op2 >0)):
                        res = - (abs(op2) // abs(op1))
                    else:
                        res = op2 // op1
                stack.append(res)
            else:
                stack.append(int(c))
        return stack.pop()

sol = Solution()
tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(sol.evalRPN(tokens))
