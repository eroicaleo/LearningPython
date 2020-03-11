#!/usr/bin/env python3

# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:
# Input: "1,#"
# Output: false
# Example 3:
# Input: "9,#,#,1"
# Output: false

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node_list = preorder.split(',')
        stack = [0] if node_list else []
        for node in node_list[1:]:
            if len(stack) == 0:
                return False
            prev = stack.pop()
            if prev == 0:
                stack.append(prev+1)
            if node != "#":
                stack.append(0)
            print(f'node = {node}, stack = {stack}')
        return (len(stack) == 0)

    def isValidSerialization2(self, preorder: str) -> bool:
        node_list, diff = preorder.split(','), 1
        for node in node_list:
            diff -= 1
            if diff < 0:
                return False
            if node != "#":
                diff += 2
            print(f'node = {node}, diff = {diff}')
        return True

    def isValidSerialization_stefan(self, preorder: str) -> bool:
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            need -= ' #'.find(val)
            print(f'val = {val}, need = {need}')
        return not need


sol = Solution()
preorder = "9,#,#,1"
preorder = "1,#"
preorder = "9,#,#,1,#,#"
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(sol.isValidSerialization(preorder))
print('Solution 2')
print(sol.isValidSerialization2(preorder))
print('Solution 3')
print(sol.isValidSerialization_stefan(preorder))
