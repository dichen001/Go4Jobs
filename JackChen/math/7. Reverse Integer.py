"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>0 else -1
        x = sign*x
        rev = 0
        while x:
            rev = rev*10 + x%10
            x /= 10
        return sign*rev * (rev<2**31)
