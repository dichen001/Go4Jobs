"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [c for c in s]
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        return ''.join(s)
