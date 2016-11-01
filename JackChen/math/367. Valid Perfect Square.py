"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        low, high = 0, num/2
        while low <= high:
            mid = (low + high) / 2
            t = mid * mid
            if t == num:
                return True
            elif t < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
