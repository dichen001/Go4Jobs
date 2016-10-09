"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [ [0] * 9 for i in range(9) ]
        cols = [ [0] * 9 for i in range(9) ]
        subs = [ [0] * 9 for i in range(9) ]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    if rows[i][num] or cols[j][num] or subs[i/3*3+j/3][num]:
                        return False
                    rows[i][num], cols[j][num], subs[i/3*3+j/3][num] = 1, 1, 1
        return True

s=Solution()
s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
