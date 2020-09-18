#!/usr/bin/env python3

class Solution:

    # if there is a q in prefixes, such that answer^1 ^ p == q
    # then it means answer^1 = answer^1 ^ p ^ p = q ^ p
    def findMaximumXOR_Stefan(self, nums):
        answer = 0
        for i in range(31,-1,-1):
            answer <<= 1
            prefixes = {num>>i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

    # Python O(n)
    # Shashwatblack
    def findMaximumXOR_Trie(self, nums):
        trie, bit_range = dict(), range(5,-1,-1)
        for n in nums:
            curr = trie
            for i in bit_range:
                bit = (n&(1<<i))>>i
                curr = curr.setdefault(bit, {})
            curr['$'] = n

        max_xor = 0
        for n in nums:
            curr = trie
            for i in bit_range:
                bit = (n&(1<<i))>>i
                curr = curr[1-bit] if (1-bit) in curr else curr[bit]
            max_xor = max(max_xor, n^curr['$'])

        return max_xor


sol = Solution()
nums = [3, 10, 5, 25, 2, 8]
print(sol.findMaximumXOR_Stefan(nums))
print(sol.findMaximumXOR_Trie(nums))
