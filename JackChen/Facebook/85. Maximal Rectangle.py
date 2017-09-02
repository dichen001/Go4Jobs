"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right, height = [0] * n, [n] * n, [0] * n
        ans = 0
        for i in range(m):
            curL, curR = 0, n
            for j in range(n):
                if matrix[i][j] == "0":
                    curL = j + 1
                    left[j] = 0
                    height[j] = 0
                else:
                    left[j] = max(left[j], curL)
                    height[j] += 1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "0":
                    curR = j
                    right[j] = n
                else:
                    right[j] = min(right[j], curR)
            for j in range(n):
                ans = max(ans, (right[j] - left[j]) * height[j])
        return ans

