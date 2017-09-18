"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1162261467=3^19. 3^20 is bigger than int.
        return n > 0 and 1162261467 % n == 0