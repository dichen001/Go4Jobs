"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
"""

import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        str = re.findall('(^[\+\-0]*\d+)', str.strip())
        if not str or str[0].count('+') + str[0].count('-') > 1:
            return 0
        pos = False if str[0].count('-') else True
        str = re.findall('\d+', str[0])
        if not str:
            return 0
        num = int(str[0]) if pos else (-1 * int(str[0]))
        if num > MAX_INT:
            return MAX_INT
        if num < MIN_INT:
            return MIN_INT
        return num


s = Solution()
s.myAtoi("-023945.324134")
