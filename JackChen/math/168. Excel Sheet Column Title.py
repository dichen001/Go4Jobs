"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = ''
        while n > 0:
            n -= 1
            i = n % 26
            i = chr(ord('A') + i)
            t = i + t
            n /= 26
        return t
