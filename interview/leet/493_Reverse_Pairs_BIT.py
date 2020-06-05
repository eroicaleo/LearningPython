#!/usr/bin/env python3

# Thinking process
# What is bit[i], it is similar to tree[idx]
# `tree[idx] = f[idx-2^r+1]+...+f[idx]`
# bit[4] covers 4/5/6/7
# bit[8] covers 8-15
# bit[i] = f[i] + ... + f[i+2^r-1]

class Solution:
    def reversePairs(self, nums) -> int:
        copy, le = sorted(list(nums)), len(nums)
        bit = [0]*(le+1)
        print(f'nums = {nums}')
        print(f'copy = {copy}')
        def index(v):
            l, r = 0, le-1
            while l <= r:
                m = l+(r-l)//2
                if copy[m] >= v:
                    r = m-1
                else:
                    l = m+1
            return l+1 # convert 0-based index to 1-based index
        def search(i): # compare to update
            s = 0
            while i <= le:
                print(f'search check {i} = {bin(i)}')
                s += bit[i]
                i += (i&-i)
                print(f'search updat {i} = {bin(i)}')
            return s
        def insert(i): # compare to read
            while i > 0:
                print(f'insert check {i} = {bin(i)}')
                bit[i] += 1
                i -= i&-i
                print(f'insert updat {i} = {bin(i)}')
        for n in nums:
            print(f'n = {n}')
            search_index = index(2*n+1)
            print(f'searching {2*n+1}, index is {search_index}')
            k = search(search_index)
            print(f'{k} elements satisfy')
            insert_index = index(n)
            print(f'inserting {n}, index is {insert_index}')
            insert(insert_index)
            print(f'bit after insertion {bit}')



sol = Solution()
nums = [2,4,3,5,1]
print(sol.reversePairs(nums))
