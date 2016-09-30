"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        for r in range(row-1):
            if target >= matrix[r][0] and target < matrix[r+1][0]:
                return self.bi_search(matrix[r], target)
        return self.bi_search(matrix[row-1], target)

    def bi_search(self, row, target):
        if len(row) <= 1:
            return target in row
        m = (len(row)-1)/2
        if row[m] == target:
            return True
        else:
            return self.bi_search(row[:m], target) or self.bi_search(row[m+1:], target)


s = Solution()
s.searchMatrix([[1,1]],0)
