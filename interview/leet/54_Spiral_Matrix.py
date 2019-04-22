#!/usr/bin/env python

class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []
        l, r, t, b, ret, direction = 0, len(matrix[0])-1, 0, len(matrix)-1, [], 0
        i, j = 0, -1
        while (l <= r) and (t <= b):
            if direction == 0:
                if j == r:
                    t, direction, i = t+1, (direction+1)%4, i+1
                else:
                    j += 1
            elif direction == 1:
                if i == b:
                    r, direction, j = r-1, (direction+1)%4, j-1
                else:
                    i += 1
            elif direction == 2:
                if j == l:
                    b, direction, i = b-1, (direction+1)%4, i-1
                else:
                    j -= 1
            elif direction == 3:
                if i == t:
                    l, direction, j = l+1, (direction+1)%4, j+1
                else:
                    i -= 1
            if l > r or t > b: break
            print('i = %d, j = %d' % (i, j))
            print('(l, r, t, b) = ', l, r, t, b)
            ret.append(matrix[i][j])
        return ret

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
matrix = [[1,2],[3,4]]
sol = Solution()
print(sol.spiralOrder(matrix))
