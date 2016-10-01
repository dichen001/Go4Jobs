"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # cell[i,j] = cell[i-1,j] + ce;;[i,j-1] if cell[i,j]!=0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        cell = [0]*col
        cell[0] = 1
        for i in range(0, row):
            for j in range(0, col):
                if obstacleGrid[i][j] == 1:
                    cell[j] = 0
                elif j > 0:
                    cell[j] += cell[j-1]
        return cell[col-1]

