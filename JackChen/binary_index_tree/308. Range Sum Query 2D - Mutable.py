"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m != 0 else 0
        if self.m == 0 or self.n == 0:
            return
        self.matrix = matrix
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return
        # self.matrix = matrix
        # self.m = len(matrix)
        # self.n = len(matrix[0])
        # for row in matrix:
        #     for col in range(1, self.n):
        #         row[col] += row[col-1]


    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0:
            return
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row+1
        while i <= self.m:
            j = col+1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i

        # if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
        #     return
        # origin = self.matrix[row][col] if col == 0 else self.matrix[row][col] - self.matrix[row][col-1]
        # delta = val - origin
        # for i in range(col, self.n):
        #     self.matrix[row][i] += delta


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0:
            return
        return self.getSum(row2+1, col2+1) + self.getSum(row1, col1) - self.getSum(row1, col2+1) - self.getSum(row2+1, col1)

        # if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
        #     return
        # result = 0
        # for row in range(row1, row2+1):
        #     row_sum = self.matrix[row][col2] if col1 == 0 else self.matrix[row][col2] - self.matrix[row][col1-1]
        #     result += row_sum
        # return result

    def getSum(self, row, col):
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return result


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
numMatrix.sumRegion(2,1,4,3)
