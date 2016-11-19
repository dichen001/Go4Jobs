"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls, lt = len(s), len(t)
        dp = [[0]*(ls+1) for i in range(lt+1)]
        for i in range(ls+1):
            dp[0][i] = 1
        for i in range(0, lt):
            for j in range(0, ls):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j] if t[i] == s[j] else dp[i+1][j]
        return dp[lt][ls]
