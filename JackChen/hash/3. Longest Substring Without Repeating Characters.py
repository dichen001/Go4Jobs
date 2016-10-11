"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        appeared, start, max_len = {}, 0, 0
        for i in range(len(s)):
            if s[i] in appeared:
                start = max(start, appeared[s[i]] + 1)
            appeared[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len
