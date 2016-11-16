"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
class Solution(object):
    def isValid2(self, board, row, col, c):
        if c == '.':
            return True
        elif c in self.row_mem.get(row, set()) or c in self.col_mem.get(col, set()) or c in self.block_mem.get(row/3 * 3 + col/3, set()):
            return False
        else:
            return True


    def update_mem(self, board, i, j, c, action):
        if action == 'add':
            self.row_mem[i] = self.row_mem.get(i).add(board[i][j]) if self.row_mem.get(i) else set(board[i][j])
            self.col_mem[j] = self.col_mem.get(i).add(board[i][j]) if self.col_mem.get(i) else set(board[i][j])
            self.block_mem[i/3 * 3 + j/3] = self.block_mem.get(i/3 * 3 + j/3).add(board[i][j]) if self.block_mem.get(i/3 * 3 + j/3) else set(board[i][j])
        else:
            self.row_mem[i].remove(board[i][j])
            self.col_mem[j].remove(board[i][j])
            self.block_mem[i/3 * 3 + j/3].remove(board[i][j])


    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isValid2(board, i, j, c):
                            s = [cc for cc in board[i]]
                            s[j] = c
                            board[i] = ''.join(s)
                            self.update_mem(board, i, j, c, 'add')
                            if self.solve(board):
                                return True
                            else:
                                s[j] = '.'
                                board[i] = ''.join(s)
                                self.update_mem(board, i, j, c, 'remove')
                    return False
        return True

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


        if not board:
            return
        self.row_mem, self.col_mem, self.block_mem = {}, {}, {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if self.row_mem.get(i):
                        self.row_mem[i].add(board[i][j])
                    else:
                        self.row_mem[i] = set(board[i][j])
                    if self.col_mem.get(j):
                        self.col_mem[j].add(board[i][j])
                    else:
                        self.col_mem[j] = set(board[i][j])
                    if self.block_mem.get(i/3 * 3 + j/3):
                        self.block_mem[i/3 * 3 + j/3].add(board[i][j])
                    else:
                        self.block_mem[i/3 * 3 + j/3] = set(board[i][j])
        self.solve(board)

s=Solution()
a = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(a)
print a
