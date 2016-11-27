"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""



"Memory Exceed"
from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = [defaultdict(int) for _ in A]
        for i in xrange(len(A)):
            for j in xrange(i):
                diff = A[i] - A[j]
                prev_count = dp[j][diff]
                result += prev_count
                dp[i][diff] += prev_count + 1
        return result



class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, dp = 0, [{} for _ in A]
        for i in xrange(len(A)):
            for j in xrange(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    result += dp[j][diff]
                    dp[i][diff] += dp[j][diff]
        return result
