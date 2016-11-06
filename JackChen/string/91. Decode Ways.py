"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        n = len(s)
        dp = [0] * (1 + n)
        dp[n] = 1
        dp[n-1] = 1 if s[n-1] != '0' else 0
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                continue
            dp[i] = dp[i+1] + dp[i+2] if int(s[i:i+2]) < 27 else dp[i+1]

        return dp[0]
