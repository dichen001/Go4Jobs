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
"""

import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        result = float('-inf')
        row, col = len(matrix), len(matrix[0])
        if row < col:
            matrix = zip(*matrix)
            row, col = col, row
        for l in range(col):
            sum = [0] * row
            for r in range(l,col):
                sum = [sum[i] + matrix[i][r] for i in range(row)]
                # find largest sum in list sum smaller than k
                # IT'S VERY IMPORTANT TO INIT accu_list with 0
                accu, accu_list = 0, [0]
                for s in sum:
                    accu += s
                    pos = bisect.bisect_left(accu_list, accu - k)
                    if pos < len(accu_list):
                        result = max(result, accu - accu_list[pos])
                    bisect.insort(accu_list, accu)
        return result

s = Solution()
s.maxSumSubmatrix([[2,2,-1]], 3)
