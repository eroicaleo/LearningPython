#!/usr/bin/env python3

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = {}
        for w in words:
            current_dict = trie
            for c in w:
                current_dict = current_dict.setdefault(c, {})
            current_dict['_end_'] = '_end_'
        print('#'*80)
        print(f'trie complete: {trie}')
        print('#'*80)
        def search(word, n):
            print(f'word = {word}, n = {n}')
            ret, current_dict = False, trie
            for i, c in enumerate(word):
                if '_end_' in current_dict:
                    ret = search(word[i:], n+1)
                    if ret:
                        return True
                if not c in current_dict:
                    return False
                current_dict = current_dict[c]
            return ('_end_' in current_dict) and (n>0)
        return [w for w in words if search(w, 0)]

sol = Solution()
words = ['cat', 'catcat', 'catcatcat']
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ['cat', 'cater', 'catercat']
print(sol.findAllConcatenatedWordsInADict(words))
