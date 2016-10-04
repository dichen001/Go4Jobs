"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        choose, num, steps = 0, 1, [n, n-1]
        matrix = [[0 for x in range(n)] for y in range(n)]
        row_id, col_id = 0, -1
        while steps[choose%2] != 0:
            for i in range(steps[choose%2]):
                row_id, col_id = row_id + directions[choose][0], col_id + directions[choose][1]
                matrix[row_id][col_id] = num
                num += 1
            steps[choose%2] -= 1
            choose = (choose + 1) % 4
        return matrix


s = Solution()
s.generateMatrix(2)
