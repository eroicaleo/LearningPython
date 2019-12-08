#!/usr/bin/env python3

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        class TrieNode:
            def __init__(self):
                self.word = False
                self.children = {}

        class Trie(object):

            def __init__(self):
                """
                Initialize your data structure here.
                """
                self.root = TrieNode()

            def insert(self, word):
                """
                Inserts a word into the trie.
                :type word: str
                :rtype: None
                """
                node = self.root
                for i in word:
                    if not i in node.children:
                        node.children[i] = TrieNode()
                    node = node.children[i]
                node.word = True

            def search(self, word):
                """
                Returns if the word is in the trie.
                :type word: str
                :rtype: bool
                """
                node = self.root
                for i in word:
                    if not i in node.children:
                        return False
                    node = node.children[i]
                return node.word

            def startsWith(self, prefix):
                """
                Returns if there is any word in the trie that starts with the given prefix.
                :type prefix: str
                :rtype: bool
                """
                node = self.root
                for i in prefix:
                    if not i in node.children:
                        return False
                    node = node.children[i]
                return True

        if len(board) == 0 or len(board[0]) == 0:
            return []
        trie = Trie()
        res = []
        lenx, leny = len(board), len(board[0])
        for w in words:
            trie.insert(w)
        def dfs(x, y, prefix, heading):
            print(heading + 'before x, y, prefix = ', x, y, prefix)
            # print(lenx, leny)
            if not ((0 <= x < lenx) and (0 <= y < leny) and board[x][y]):
                print(heading + 'out of range or visited')
                return
            c = board[x][y]
            board[x][y] = ''
            newPrefix = prefix + c
            if trie.search(newPrefix):
                res.append(newPrefix)
            elif trie.startsWith(newPrefix):
                for i, j in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    dfs(i, j, newPrefix, heading+'  ')
            print(heading + 'after x, y, prefix = ', x, y, prefix)
            board[x][y] = c
        [dfs(x, y, '', '') for x in range(lenx) for y in range(leny)]
        return res

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))
# print(board)
