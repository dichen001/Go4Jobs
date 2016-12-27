"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def outer():
    x = 0
    def inner():
        print x
    inner()
    print x

outer()


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        low, ans = 0, 0
        for i, c in enumerate(s):
            if mem.get(c):
                low = mem[c] + 1
            mem[c] = i
            ans = max(ans, i - low + 1)
        return ans


        appeared, start, max_len = {}, 0, 0
        for i in range(len(s)):
            if s[i] in appeared:
                start = max(start, appeared[s[i]] + 1)
            appeared[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len

s =Solution()
s.lengthOfLongestSubstring("abcabcbb")
