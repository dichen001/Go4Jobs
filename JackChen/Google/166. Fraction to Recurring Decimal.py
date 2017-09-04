"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, d = numerator, denominator
        if n == 0: return '0'
        if d == 0: return "NaN"
        ans = [] if (n > 0) == (d > 0) else ['-']
        n, d = abs(n), abs(d)
        q, r = n / d, n % d
        ans.append(str(q))
        if r == 0:
            return "".join(ans)
        ans.append('.')
        mem = {}
        while r:
            if r in mem:
                i = mem[r]
                ans = ans[:i] + ['('] + ans[i:] + [')']
                break
            mem[r] = len(ans)
            r *= 10
            ans.append(str(r/d))
            r %= d
        return ''.join(ans)