#!/usr/bin/env python

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.count = 0
        if len(matrix) > 0 and len(matrix[0]) > 0:
            return self.search2DArray(matrix, target, 0, 0, len(matrix)-1, len(matrix[0])-1)
        return False

    def search2DArray(self, matrix, target, i0, j0, i1, j1):
        self.count += 1
        if self.count > 50:
            return False
        print("i0, j0, i1, j1 = ", (i0, j0, i1, j1))
        if i0 > i1 or j0 > j1:
            return False
        midi = (i1+i0)//2
        midj = (j0+j1)//2
        bot = matrix[i1][midj]
        top = matrix[i0][midj]
        lft = matrix[midi][j0]
        rit = matrix[midi][j1]
        mid = matrix[midi][midj]
        print('(bot, top, lft, rit, mid) = ', (bot, top, lft, rit, mid))
        if target in (bot, top, lft, rit, mid):
            print('hit the target: ', (bot, top, lft, rit, mid))
            return True
        if target > bot:
            print('I am in 1')
            return self.search2DArray(matrix, target, i0, midj+1, i1, j1)
        if target < top:
            print('I am in 2')
            return self.search2DArray(matrix, target, i0, j0, i1, midj-1)
        if target > rit:
            print('I am in 3')
            return self.search2DArray(matrix, target, midi+1, j0, i1, j1)
        if target < lft:
            print('I am in 4')
            return self.search2DArray(matrix, target, i0, j0, midi-1, j1)

        print('I am in region1')
        region1 = self.search2DArray(matrix, target, i0, midj, midi, j1)
        if region1 == True:
            return True
        print('I am in region2')
        region2 = self.search2DArray(matrix, target, midi, j0, i1, midj)
        if region2 == True:
            return True
        if target < mid:
            print('I am in 5')
            region3 = self.search2DArray(matrix, target, i0, j0, midi-1, midj-1)
        elif target > mid:
            print('I am in 6')
            region3 = self.search2DArray(matrix, target, midi+1, midj+1, i1, j1)
        return region3

sol = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
matrix = [
        [ 48,  65,  70, 113, 133, 163, 170, 216, 298, 389],
        [ 89, 169, 215, 222, 250, 348, 379, 426, 469, 554],
        [178, 202, 253, 294, 367, 392, 428, 434, 499, 651],
        [257, 276, 284, 332, 380, 470, 516, 561, 657, 698],
        [275, 331, 391, 432, 500, 595, 602, 673, 758, 783],
        [357, 365, 412, 450, 556, 642, 690, 752, 801, 887],
        [359, 451, 534, 609, 654, 662, 693, 766, 803, 964],
        [390, 484, 614, 669, 684, 711, 767, 804, 857,1055],
        [400, 515, 683, 732, 812, 834, 880, 930,1012,1130],
        [480, 538, 695, 751, 864, 939, 966,1027,1089,1224]]

# print(sol.searchMatrix(matrix, 5))
print(sol.searchMatrix(matrix, 642))
