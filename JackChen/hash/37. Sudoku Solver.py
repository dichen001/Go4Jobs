"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] != '.' and board[row][i] == c:
                    return False
                if board[i][col] != '.' and board[i][col] == c:
                    return False
                x, y = 3 * (row / 3) + i / 3, 3 * (col / 3) + i % 3
                if board[x][y] != '.' and board[x][y] == c:
                    return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in '123456789':
                            if isValid(board, i, j, c):
                                board[i] = board[i][:j] + c + board[i][j+1:]
                                if solve(board):
                                    return True
                                else:
                                    board[i] = board[i][:j] + '.' + board[i][j+1:]
                        return False
            return True
        if not board:
            return
        solve(board)

s=Solution()
a = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(a)
print a
