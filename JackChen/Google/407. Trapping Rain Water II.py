"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water are trapped between the blocks. The total volume of water trapped is 4.
"""

import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m , n = len(heightMap), len(heightMap[0])
        visited = [[0] * n for _ in range(m)]
        queue = []
        water = 0
        for i in range(m):
            visited[i][0] = visited[i][n-1] = 1
            heapq.heappush(queue, (heightMap[i][0], i, 0))
            heapq.heappush(queue, (heightMap[i][n-1], i, n-1))
        for j in range(n):
            visited[0][j] = visited[m-1][j] = 1
            heapq.heappush(queue, (heightMap[0][j], 0, j))
            heapq.heappush(queue, (heightMap[m-1][j], m-1, j))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            cell = heapq.heappop(queue)
            h, i, j = cell[0], cell[1], cell[2]
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    water += max(0, h - heightMap[ni][nj])
                    visited[ni][nj] = 1
                    heapq.heappush(queue, (max(h, heightMap[ni][nj]), ni, nj))
        return water


