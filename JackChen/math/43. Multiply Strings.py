"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        r, s = 0, []
        for i, n1 in enumerate(num1[::-1]):
            m1 = ord(n1) - ord('0')
            d = 0
            for j, n2 in enumerate(num2[::-1]):
                m2 = ord(n2) - ord('0')
                d += (m1 * m2) * 10**j
            r += d * 10**i
        while r:
            s.insert(0, str(r%10))
            r /= 10
        return ''.join(s) if s else '0'


        # recursive
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
