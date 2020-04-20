#!/usr/bin/env python3

class Solution:
    def reversePairs(self, nums) -> int:
        def merge(src, dst, lo, hi):
            if lo >= hi:
                return 0
            mi = lo+(hi-lo)//2
            l, r, ret = merge(dst, src, lo, mi), merge(dst, src, mi+1, hi), 0
            i, j, rp = lo, mi+1, lo
            for k in range(lo,hi+1):
                if (i > mi) or (j <= hi and src[j] > src[i]):
                    while (src[rp] > 2*src[j]) and rp <= mi:
                        rp += 1
                    ret += rp-lo
                    dst[k], j = src[j], j+1
                else:
                    dst[k], i = src[i], i+1
            ret = ret+l+r
            print(f'lo = {lo}, hi = {hi}, {dst[lo:hi+1]}, {ret}')
            return ret
        nums_aux = [n for n in nums]
        ret = merge(nums_aux, nums, 0, len(nums)-1)
        print(nums)
        return ret 

sol = Solution()
nums = [2,4,3,5,1]
nums = [1,3,2,3,1]
print(sol.reversePairs(nums))
