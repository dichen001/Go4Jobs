class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def dfs(i, j):
            if (i >= len(s) and j >= len(p)) or (j == len(p) - 1 and p[j] == '*'):
                return True
            if i >= len(s) or j >= len(p):
                return False
            if s[i] != p[j] and p[j] not in "?*":
                return False
            if s[i] == p[j] or p[j] == '?':
                return dfs(i + 1, j + 1)
            if p[j] == '*':
                for ii in range(i, len(s)):
                    if (i == ii and dfs(ii, j + 1)) or (i != ii and dfs(ii, j) or dfs(ii, j + 1)):
                        return True
            return False

        return dfs(0, 0)


s = Solution()
s.isMatch('ho', 'ho**')