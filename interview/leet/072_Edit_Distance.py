#!/usr/bin/env python

# idea: dynamic programming, similar to longest common sequence
#    Ø, r, o, s
# Ø [0, 1, 2, 3]
# h [1, 1, 2, 3]
# o [2, 2, 1, 2]
# r [3, 2, 2, 2]
# s [4, 3, 3, 2]
# e [5, 4, 4, 3]

# assume we want to find the minDistance between word1[0:i] and word2[0:j]
# Then if would come from:
# 1. minDistance between word1[0:i-1] and word2[0:j] and delete word1[i]
# 2. minDistance between word1[0:i] and word2[0:j-1] and add word1[i]
# 3. minDistance between word1[0:i-1] and word2[0:j-1] and replace word1[i] with word2[i] if they are different

# About initialization the first row and column
# 1. First row, you want to match (Ø, Ø), do nothing, (Ø, r), insert 1, (Ø, ro), insert 2
# 1. First col, you want to match (Ø, Ø), do nothing, (h, Ø), delete 1, (ho, Ø), delete 2

# Optimization
# Because it only needs one way travel, we just need to maintain one row

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1) + 1, len(word2) + 1
        table = [list(range(n2)) for i in range(n1)]
        for i in range(1, n1):
            table[i][0] = i
            for j in range(1, n2):
                d = min(table[i][j-1]+1, table[i-1][j]+1)
                if word1[i-1] == word2[j-1]:
                    table[i][j] = min(d, table[i-1][j-1])
                else:
                    table[i][j] = min(d, table[i-1][j-1]+1)
        print('   Ø, ' + ', '.join(list(word2)))
        for i in range(n1):
            print(('Ø'+word1)[i], table[i])
        return table[n1-1][n2-1]

sol = Solution()
word1, word2 = "inten", "execu"
word1, word2 = "intention", "execution"
word1, word2 = '', 'a'
word1, word2 = 'a', ''
word1, word2 = '', ''
word1, word2 = "horse", "ros"
print(sol.minDistance(word1, word2))
