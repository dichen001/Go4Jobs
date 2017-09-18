"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # O(1)  the max possible power of two = 2^30 = 1073741824.
        return n > 0 and (2 ** 30 % n == 0);

        # O(1)
        return False if n <= 0 else not (n & (n - 1))

        # O(logN)
        while n > 1:
            if n % 2 == 1:
                return False
            n /= 2
        return n == 1

