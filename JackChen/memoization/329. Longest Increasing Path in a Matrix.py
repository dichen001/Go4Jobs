"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            if dist[i][j] > -1:
                return dist[i][j]
            dist[i][j] = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    dist[i][j] = max(dist[i][j], 1 + dfs(ni, nj))
            result[0] = max(result[0], dist[i][j])
            return dist[i][j]

        if not matrix or len(matrix[0]) < 1:
            return 0
        m, n = len(matrix), len(matrix[0])
        dist = [[-1] * n for _ in range(m)]
        result = [0]
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return result[0]