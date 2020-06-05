#!/usr/bin/env python3

class Solution:
    def replaceWords(self, dict, sentence) -> str:
        trie = {}
        for word in dict:
            current_dict = trie
            for c in word:
                current_dict = current_dict.setdefault(c, {})
            current_dict['_end_'] = '_end_'
        print(trie)
        def search(word):
            current_dict = trie
            for i, c in enumerate(word):
                if '_end_' in current_dict:
                    return word[:i]
                elif not c in current_dict:
                    break
                current_dict = current_dict[c]
            return word
        return list(map(search, sentence.split()))

d = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print(sol.replaceWords(d, sentence))
