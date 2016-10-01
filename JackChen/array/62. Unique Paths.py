"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """


        "directly solve by calculation"

        # Total (m-1) + (n-1) steps
        # Need m-1 steps down,  or n-1 steps right.
        # So C(m+n-2, n-1)

        """
        result = 1
        for i in range(1,n):
            result = result * (m+n-1-i) / (i)
        return result
        """


        "dynamic programming"

        # The idea is really simple. cell[i,j] = cell[i-1,j] + cell[i, j-1] for i>0,j>0
        # Edge condition is cell[0,j]=1 and cell[i,0]=1
        #
        # Then think further, cell[i-1,j] == cell[i, j-1] cause the symmetry of matrix.
        # So we only need consider one direction.
        # cell[j] = cell[j] + cell[j-1]

        cell = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                cell[j] += cell[j-1]
        return cell[n-1]





s = Solution()
s.uniquePaths(1,3)
