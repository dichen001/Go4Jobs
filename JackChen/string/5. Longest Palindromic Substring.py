"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

class Solution(object):
    def __init__(self):
        self.start = 0
        self.max_len = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Don't be traped in one way (from outter to central part),
        ## try to look at the other way (from central part to outer)!

        for i in range(len(s)):
            self.findP(s, i, i)
            self.findP(s, i, i + 1)
        return s[self.start: self.start + self.max_len]

    def findP(self, s, i,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i-1, j+1
        if self.max_len < j-i-1:
            self.max_len = j-i-1
            self.start = i+1
