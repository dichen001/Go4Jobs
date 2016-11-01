"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -1*2**31 and divisor == -1):
            return 2**31 - 1
        sign = -1 if (divisor > 0) != (dividend > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp_dvs, tmp_result = divisor, 1
            while dividend >= (tmp_dvs << 1):
                tmp_dvs = tmp_dvs << 1
                tmp_result = tmp_result << 1
            dividend -= tmp_dvs
            result += tmp_result
        return sign * result
