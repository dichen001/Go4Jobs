"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        result, row_hits = 0, 0
        col_hits = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        row_hits += grid[i][k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        col_hits[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, row_hits + col_hits[j])
        return result

s = Solution()
s.maxKilledEnemies(["0E00","E0WE","0E00"])
