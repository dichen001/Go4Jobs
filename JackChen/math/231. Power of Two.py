"""
Given an integer, write a function to determine if it is a power of two.

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (math.log10(n)/math.log10(2)).is_integer()
