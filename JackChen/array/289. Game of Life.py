"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        ## 00 : dead -> die   0
        ## 01 : live -> die   1
        ## 10 : dead -> live  2
        ## 11 : live -> live  3
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 and self.nearby(board,i,j) == 3:
                        board[i][j] = 2
                if board[i][j] == 1 and self.nearby(board,i,j) in [2,3]:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] /= 2

    def nearby(self, board, i, j):
        m,n = len(board), len(board[0])
        count = 0
        for ii in range(max(i-1,0), min(i+2, m)):
            for jj in range(max(j-1,0), min(j+2, n)):
                if board[ii][jj] in [1, 3]:
                    count += 1
        count -= board[i][j]%2
        return count

s = Solution()
s.gameOfLife([[1,1],[1,0]])
