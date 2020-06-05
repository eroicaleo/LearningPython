#!/usr/bin/env python3

import math

class RMQ:
    def __init__(self, a):
        self.a = a
        self.MAXN = len(a)
        self.LOGMAXN = math.ceil(math.log2(self.MAXN))
        self.process_st()
        assert self.check_st()

    def process_st(self):
        self.M = [[0]*self.LOGMAXN for i in range(self.MAXN)]
        for i in range(self.MAXN):
            self.M[i][0] = i
        print('self.M: j = 0')
        for row in self.M:
            print(row)
        j = 1
        while (1 << j) <= self.MAXN:
            # Assume N = 10, j = 1, i = [0,8], M[8][1] covers A[8], A[9]
            # Assume N = 10, j = 2, i = [0,6], M[6][2] covers A[6,7,8,9]
            # Assume N = 10, j = 3, i = [0,2], M[2][3] covers A[2,3,4,5,6,7,8,9]
            for i in range(self.MAXN+1-(1<<j)):
                # j = 1, update M[0][1], compare A[0,1], M[0][0] is A[0], M[1][0] is A[1]
                # j = 2, update M[0][2], compare A[0,1,2,3], M[0][1] is A[0,1], M[2][1] is A[2,3]
                if self.a[self.M[i][j-1]] <= self.a[self.M[i+(1<<(j-1))][j-1]]:
                    self.M[i][j] = self.M[i][j-1]
                else:
                    self.M[i][j] = self.M[i+(1<<(j-1))][j-1]

            print(f'self.M: j = {j}')
            for row in self.M:
                print(row)
            j += 1

    def query_st(self, i, j):
        # i = 0, j = 15, k = 4
        # i = 0, j = 7, k = 3
        # i = 0, j = 9, k = 3
        k = math.floor(math.log2(j-i+1))
        # print(f'i = {i}, j = {j}, k = {k}, j-(1<<k)+1 = {j-(1<<k)+1}')
        if self.a[self.M[i][k]] <= self.a[self.M[j-(1<<k)+1][k]]:
            return self.M[i][k]
        else:
            return self.M[j-(1<<k)+1][k]

    def check_st(self):
        for i in range(self.MAXN):
            for j in range(i, self.MAXN):
                if self.a[self.query_st(i, j)] != min(self.a[i:j+1]):
                    print(f'check_st: i = {i}, j = {j}, index {self.query_st(i, j)} is {self.a[self.query_st(i, j)]}')
                    return False
        return True

if __name__ == '__main__':
    a = [2,4,3,1,6,7,8,9,1,7]
    rmq = RMQ(a)
    print(f'rmq = {rmq.a}')
    print(f'MAXN = {rmq.MAXN}')
    print(f'LOGMAXN = {rmq.LOGMAXN}')
