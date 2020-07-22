#!/usr/bin/env python3

class Solution:
    def palindromePairs(self, words):
        trie, ret = {}, []
        def isPalindrome(w):
            return w == w[::-1]
        for i, word in enumerate(words):
            t, rword = trie, word[::-1]
            for k, c in enumerate(rword):
                if isPalindrome(rword[k:]):
                    t.setdefault('%', []).append(i)
                t = t.setdefault(c, {})
            t.setdefault('$', i)
        print(trie)
        for i, word in enumerate(words):
            t = trie
            for k, c in enumerate(word):
                if isPalindrome(word[k:]) and ('$' in t):
                    ret += [[i, t['$']]]
                if c in t:
                    t = t[c]
                else:
                    break
            else:
                if '%' in t:
                    ret += [[i, j] for j in t['%']]
                if '$' in t and t['$'] != i:
                    ret += [[i, t['$']]]
        return ret

 
sol = Solution()
words = ["abccb", ""]
words = ["abc", 'ba']
words = ["a", ""]
words = ["ab","a","ba"]
words = ["s","sll"]
words = ["s","sssll"]
words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat"]
words = ["abba"]
print(sol.palindromePairs(words))
