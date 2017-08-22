class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.m, self.n = m, n
        self.matrix = [[0] * n for _ in range(m)]
        self.BIT = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        m, n = self.m, self.n
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i < m + 1:
            j = col + 1
            while j < n + 1:
                self.BIT[i][j] += diff
                j += j & -j
            i += i & -i


    def getSum(self, row, col):
        ret = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                ret += self.BIT[i][j]
                j -= j & -j
            i -= i & -i
        return ret


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        S = self.getSum
        return S(row2, col2)  - S(row2, col1-1) - S(row1-1, col2) + S(row1-1, col1-1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
numMatrix.sumRegion(2,1,4,3)
