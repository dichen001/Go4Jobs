"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = [i for i, c in enumerate(s) if c.lower() in "aeiou"]
        l, r = 0, len(idx) - 1
        ret = [c for c in s]
        while l < r:
            ret[idx[l]], ret[idx[r]] = ret[idx[r]], ret[idx[l]]
            l, r = l + 1, r - 1
        return "".join(ret)
