"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m1, m2, m3 = len(A), len(A[0]), len(B[0])
        memA = collections.defaultdict(list)
        # O(m1*m2)
        for i in range(m1):
            for j in range(m2):
                if A[i][j] != 0:
                    memA[i] += [j]
        # O(m2*m3)
        # memB = [i for i in range(m3) if set(B[:][i]) != {0}]

        C = [[0] * m3 for _ in range(m1)]
        for i in memA.iterkeys():
            # for j in memB:
            for j in range(m3):
                for k in memA[i]:
                    C[i][j] += A[i][k] * B[k][j]
        return C