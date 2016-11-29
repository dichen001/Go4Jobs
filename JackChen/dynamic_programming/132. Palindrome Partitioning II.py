"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, result = len(s), -1
        dp = [[False] * n for _ in range(n)]
        for i in range(n)[::-1]:
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
        def findAll(start, path):
            global result
            if start == n:
                result = min(result, len(path) - 1)
                return
            for i in range(start, n)[::-1]:
                if dp[start][i]:
                    path.append(s[start:i+1])
                    findAll(i+1, path)
                    path.pop()
        findAll(0, [])
        return result

s = Solution()
s.minCut('aab')
