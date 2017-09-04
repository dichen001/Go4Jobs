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
        # # most intuitive version; faster but waster space
        # if not grid or not grid[0]:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # row_sum, col_sum = [0] * m, [0] * n
        # row_visited, col_visited = [False] * m, [False] * n
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "W":
        #             row_visited[i] = col_visited[j] = False
        #             row_sum[i] = col_sum[j] = 0
        #             continue
        #         if not row_visited[i]:
        #             row_visited[i] = True
        #             jj = j
        #             while jj < n and grid[i][jj] != 'W':
        #                 row_sum[i] += grid[i][jj] == 'E'
        #                 jj += 1
        #         if not col_visited[j]:
        #             col_visited[j] = True
        #             ii = i
        #             while ii < m and grid[ii][j] != 'W':
        #                 col_sum[j] += grid[ii][j] == 'E'
        #                 ii += 1
        #         if grid[i][j] == '0':
        #             ans = max(ans, row_sum[i] + col_sum[j])
        # return ans

        # optimized version.
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        row_sum, col_sum = 0, [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == "W":
                    row_sum = 0
                    jj = j
                    while jj < n and grid[i][jj] != 'W':
                        row_sum += grid[i][jj] == 'E'
                        jj += 1
                if i == 0 or grid[i - 1][j] == "W":
                    col_sum[j] = 0
                    ii = i
                    while ii < m and grid[ii][j] != 'W':
                        col_sum[j] += grid[ii][j] == 'E'
                        ii += 1
                if grid[i][j] in 'E0':
                    ans = max(ans, row_sum + col_sum[j])
        return ans


s = Solution()
s.maxKilledEnemies(["0E00","EEWE","0E00"])
