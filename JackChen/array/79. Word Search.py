"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, i, j, word, start= 0):
                    return True
        return False
    def check(self, board, y, x, word, start):
        if start == len(word): return True
        if x<0 or y<0 or y>=len(board) or x>=len(board[0]) or word[start]!= board[y][x]: return False
        tmp = board[y][x]
        board[y][x] = '#'
        result = self.check(board, y-1, x, word, start+1) or self.check(board, y, x-1, word, start+1) \
                or self.check(board, y+1, x, word, start+1) or self.check(board, y, x+1, word, start+1)
        board[y][x] = tmp
        return result
