"""
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""
import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n, result = len(matrix), len(matrix[0]), float('-inf')
        if n > m:
            matrix = zip(*matrix)
            m, n = n, m
        for l in range(n):
            col_sum = [0] * m
            for r in range(l, n):
                col_sum = [col_sum[i] + matrix[i][r] for i in range(m)]
                block_sum, block_sums = 0, [0]
                for cs in col_sum:
                    block_sum += cs
                    pos = bisect.bisect_left(block_sums, block_sum - k)
                    if pos < len(block_sums):
                        result = max(result, block_sum - block_sums[pos])
                    bisect.insort(block_sums, block_sum)
        return result
