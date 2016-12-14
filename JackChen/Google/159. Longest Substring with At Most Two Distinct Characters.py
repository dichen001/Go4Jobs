"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        ans = 0
        low = 0
        for i, c in enumerate(s):
            mem[c] = i
            if len(mem) > 2:
                low = min(mem.values())
                del mem[s[low]]
                low += 1
            ans = max(ans, i - low + 1)
        return ans
