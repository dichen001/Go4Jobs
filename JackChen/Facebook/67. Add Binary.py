"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = list(a), list(b)
        ans, c = [], 0
        while a or b:
            i = int(a.pop()) if a else 0
            j = int(b.pop()) if b else 0
            ans.append("1" if i + j + c in [1, 3] else "0")
            c = i + j + c > 1
        if c == 1:
            ans.append("1")
        return "".join(ans)[::-1]
