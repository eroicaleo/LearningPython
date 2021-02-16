#!/usr/bin/env python3

class Solution:
    def buddStrings(self, A, B):
        la, lb = len(A), len(B)
        if la != lb:
            return False
        diff = [i for i in range(la) if A[i] != B[i]]
        if len(diff) > 2 or len(diff) == 1:
            return False
        elif len(diff) == 0 and len(set(A)) == la:
            return False
        else:
            i, j = diff
            if A[i] != B[j] or A[j] != B[i]:
                return False
        return True

