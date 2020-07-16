#!/usr/bin/env python3

class Solution(object):
    def findWords(self, board, words):
        trie = dict()
        for word in words:
            current_dict = trie
            for c in word:
                current_dict = current_dict.setdefault(c, {})
            current_dict['$'] = word
        nr, nc = len(board), len(board[0])
        delta = [(1,0),(-1,0),(0,1),(0,-1)]
        self.ret = set()
        def dfs(i, j, current_dict):
            print(f'i = {i}, j = {j}, current_dict = {current_dict}')
            c, board[i][j] = board[i][j], ''
            if '$' in current_dict:
                self.ret.add(current_dict['$'])
            for dx, dy in delta:
                v, w = i+dx, j+dy
                if 0 <= v < nr and 0 <= w < nc and board[v][w] in current_dict:
                    dfs(v, w, current_dict[board[v][w]])
            board[i][j] = c
        for i in range(nr):
            for j in range(nc):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]])
        return self.ret

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
words = ["oath","pea","eat","oat"]
board = [['a', 'a']]
words = ['a']
sol = Solution()
print(sol.findWords(board, words))
