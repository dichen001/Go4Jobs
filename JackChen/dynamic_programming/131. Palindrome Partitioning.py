"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n, result = len(s), []
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
        def findAll(start, path):
            if start == n:
                result.append(path[:])
                return
            for i in range(start, n):
                if dp[start][i]:
                    path.append(s[start:i+1])
                    findAll(i+1, path)
                    path.pop()
        findAll(0, [])
        return result

s = Solution()
s.partition('aab')
