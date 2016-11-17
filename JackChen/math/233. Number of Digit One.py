"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        r, l, a, x = n , 0, 0, 1
        while r > 0:
            d = r % 10
            r /= 10
            l = n % x
            a += r * x
            if d == 1:
                a += l + 1
            if d > 1:
                a += x
            x *= 10
        return a
