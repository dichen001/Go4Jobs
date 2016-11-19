
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False for i in range(lp + 1)] for j in range(ls + 1)]
        dp[0][0] = True
        for i in range(2, lp + 1):
            if dp[0][i-2] and p[i-1] == '*':
                dp[0][i] = True
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    if p[j-2] != '.' and p[j-2] != s[i-1]:
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
        return dp[-1][-1]


s = Solution()
s.isMatch("aaa", "ab*ac*a")
