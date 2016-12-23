"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [[0,0] for _ in range(n)]
        self.cols = [[0,0] for _ in range(n)]
        self.diagonal = [[0,0], [0,0]]


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.rows[row][player-1] += 1
        self.cols[col][player-1] += 1
        if row == col:
            self.diagonal[0][player-1] += 1
        if row + col == self.n - 1:
            self.diagonal[1][player-1] += 1
        n = self.n
        if n in [self.rows[row][player-1], self.cols[col][player-1], self.diagonal[0][player-1], self.diagonal[1][player-1]]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
