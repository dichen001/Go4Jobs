"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        "Second Try"
        ids, idp, ls, lp = 0, 0, len(s), len(p)
        next_p = -1
        while ids < ls:
            if idp < lp and (p[idp] == '?' or p[idp] == s[ids]):
                idp += 1
                ids += 1
                continue
            if idp < lp and p[idp] == '*':
                start_s = ids
                idp += 1
                next_p = idp
                continue
            if next_p > -1:
                idp = next_p
                start_s += 1
                ids = start_s
                continue
            return False
        while idp < lp and p[idp] == '*':
            idp += 1
        return idp >= lp



        "First Try. Used the general DP solution, which meet the TLE... Cause the "
        ls, lp = len(s), len(p)
        dp = [[False] * (lp+1) for _ in range(ls+1)]
        # dp[i][j] indicates wheather s[i-1:] and p[j-1:] matches
        # so dp[ls][lp] simply says s[ls-1:] and p[lp-1:] which are '' and '' matches
        for i in range(lp,-1,-1):
            if i == lp or p[i] == '*':
                dp[ls][i] = True
            else:
                break
        for i in range(ls-1,-1,-1):
            for j in range(lp-1,-1,-1):
                if p[j] == s[i] or p[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                if p[j] == '*':
                    dp[i][j] = dp[i+1][j+1] or dp[i][j+1] or dp[i+1][j]
        return dp[0][0]

