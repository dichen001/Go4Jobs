"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        flag_row, flag_col = False, False
        if  0 in matrix[0]:
            flag_row = True
        if 0 in [matrix[i][0] for i in range(row)]:
            flag_col = True
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, row):
            if matrix[r][0] == 0:
                matrix[r] = [0]*col
        for c in range(1, col):
            if matrix[0][c] == 0:
                for i in range(row):
                    matrix[i][c] = 0

        if flag_row:
            matrix[0] = [0] * col
        if flag_col:
            for i in range(row):
                matrix[i][0] = 0


"1st row is enough for labeling"

def setZeroes(self, matrix):
    # First row has zero?
    m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
    # Use first row/column as marker, scan the matrix
    for i in xrange(1, m):
        for j in xrange(n):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0
    # Set the zeros
    for i in xrange(1, m):
        for j in xrange(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Set the zeros for the first row
    if firstRowHasZero:
        matrix[0] = [0] * n
