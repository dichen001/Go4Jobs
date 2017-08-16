"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(node, i, j):
            if node.get('end'):
                ans.append(node['end'])
                node['end'] = None
                return
            c = board[i][j]
            board[i][j] = "#"
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#' and board[ni][nj] in node[c]:
                    dfs(node[c], ni, nj)
            board[i][j] = c

        if not words or not words[0]:
            return []
        # build Trie
        root, ans = {}, []
        for w in words:
            node = root
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['end'] = w
        # dfs
        m, n = len(words), len(words[0])
        for i in range(m):
            for j in range(n):
                dfs(root, i, j)
        return ans

s = Solution()
s.findWords([["a","a"]],["a"])