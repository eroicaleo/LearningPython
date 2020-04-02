#!/usr/bin/env python3

class Solution:
    def palindromePairs(self, words):
        trie, ret = {}, []
        def isPalindrome(w, i):
            j, l = 0, len(w)
            print(f'isPalindrome: w={w}, i={i}')
            while i+j+j < l:
                if w[i+j] != w[l-1-j]:
                    return False
                j += 1
            return True
        for i, w in enumerate(words):
            wr = w[::-1]
            current_dict = trie
            for j, c in enumerate(wr):
                print(f'before trie = {trie}, current_dict = {current_dict}')
                if isPalindrome(wr, j):
                    print(f'isPalindrome: wr={wr}, j+1={j+1} is True')
                    current_dict.setdefault('_padlindrome_', []).append(i)
                current_dict = current_dict.setdefault(c, {})
            current_dict.setdefault('_end_', []).append(i)
            print(f'after trie = {trie}, current_dict = {current_dict}')
        print('#'*80)
        print(f'trie complete: {trie}')
        print('#'*80)
        for i, w in enumerate(words):
            current_dict = trie
            for j, c in enumerate(w):
                if c not in current_dict:
                    break
                if ('_end_' in current_dict) and isPalindrome(w, j):
                    ret += [[i, k] for k in current_dict['_end_'] if k != i]
                current_dict = current_dict[c]
            for key in ['_padlindrome_', '_end_']:
                if (key in current_dict) and isPalindrome(w, j):
                    ret += [[i, k] for k in current_dict[key] if k != i]
        return ret

sol = Solution()
words = ["abc"]
words = ["abc", 'ba']
words = ["bcba", 'bccba']
words = ["abcd"]
words = ["abba"]
words = ["ab","a","ba"]
words = ["bat","tab","cat"]
words = ["", "aba"]
words = ["s","sssll"]
words = ["s","sll"]
words = ["a", ""]
words = ["abcd","dcba","lls","s","sssll"]
print(sol.palindromePairs(words))

# w = 'sssll'
# w = 'lls'
# w = 'sll'
# w = 'slls'
# w = 'abcd'
# def isPalindrome(w, i):
#     j, l = 0, len(w)
#     while i+j+j < l:
#         if w[i+j] != w[l-1-j]:
#             return False
#         j += 1
#     return True
#  
# for i in range(len(w)):
#     print(f'w = {w}, i = {i}, {isPalindrome(w, i)}')
