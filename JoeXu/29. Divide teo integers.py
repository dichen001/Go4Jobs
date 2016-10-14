class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT=2147483647
        a=abs(dividend)
        b=abs(divisor)
        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        ret, c = 0, 0
        while a >= b:
            c = b
            i = 0
            while a >= c:
                a -= c
                ret += (1<<i)
                i += 1
                c <<= 1
        if sign:
            ret = -ret
        return min(max(-MAX_INT-1, ret), MAX_INT)