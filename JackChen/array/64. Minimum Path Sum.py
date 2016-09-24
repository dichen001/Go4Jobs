"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c != 0:
                    grid[r][c] += grid[r][c-1]
                if r != 0 and c == 0:
                    grid[r][c] += grid[r-1][c]
                if r != 0 and c != 0:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[r][c]


                    