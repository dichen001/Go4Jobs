"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return num1 + num2
        i, j = len(num1) - 1, len(num2) - 1
        ans, carry = [], 0
        while i > -1 or j > -1 or carry:
            x = int(num1[i]) if i > -1 else 0
            y = int(num2[j]) if j > -1 else 0
            z = x + y + carry
            carry = z / 10
            ans.append(str(z % 10))
            i, j = i - 1, j - 1
        if carry:
            ans.append("1")
        return "".join(ans[::-1])
