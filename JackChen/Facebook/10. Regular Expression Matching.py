"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False] * (lp+1) for _ in range(ls+1)]
        dp[0][0] = True
        for j in range(2, lp+1):
            if p[j-1] == "*" and dp[0][j-2]:
                dp[0][j] = True
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if p[j-2] != s[i-1] and p[j-2] != ".":
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
        return dp[ls][lp]