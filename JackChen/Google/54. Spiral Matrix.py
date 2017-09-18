"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # optimazed
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        steps = [n, m - 1]
        d, D = 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans, i, j = [], 0, -1
        while steps[d % 2] > 0:
            for _ in range(steps[d % 2]):
                i, j = i + D[d][0], j + D[d][1]
                ans.append(matrix[i][j])
            steps[d % 2] -= 1
            d = (d + 1) % 4
        return ans

        # 1st try
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        unvisited = m * n
        ans, i, j = [], 0, -1
        while unvisited > 0:
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i, j = i + di, j + dj
                while unvisited > 0 and 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    visited[i][j] = True
                    unvisited -= 1
                    ans.append(matrix[i][j])
                    i, j = i + di, j + dj
                i, j = i - di, j - dj
        return ans