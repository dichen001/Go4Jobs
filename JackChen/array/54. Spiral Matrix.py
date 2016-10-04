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
        if not matrix:
            return []
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        steps = [len(matrix[0]), len(matrix)-1]
        choose, result = 0, []
        row_id, col_id = 0, -1
        while steps[choose%2] != 0:
            for i in range(steps[choose%2]):
                row_id, col_id = row_id + directions[choose][0], col_id + directions[choose][1]
                result.append(matrix[row_id][col_id])
            steps[choose%2] -= 1
            choose = (choose + 1) % 4
        return result
