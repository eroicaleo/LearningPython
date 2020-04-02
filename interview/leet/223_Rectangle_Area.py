#!/usr/bin/env python3

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a, b = min(C,G)-max(A,E), min(D,H)-max(B,F)
        return (C-A)*(D-B)+(G-E)*(H-F)-max(0,a)*max(0,b)

sol = Solution()
A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2

A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 0

A = 0
B = 0
C = 3
D = 2
E = 0
F = -1
G = 9
H = 2


print(sol.computeArea(A,B,C,D,E,F,G,H))
