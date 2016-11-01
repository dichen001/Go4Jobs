"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # newton's methods:
        # f(x) = r^2 - x = 0
        # x(i+1) = x(i) - f(x(i))/f'(x(i))

        r = x
        while r*r > x:
            # k = 2*r   # k = h/d
            # h = r*r - x
            # r = r - h/k
            r = (r + x/r) / 2
        return r
