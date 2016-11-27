"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # if s in wordDict:
        #     return True
        # for i in range(1, len(s)):
        #     if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
        #         return True
        # return False
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1,n+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        return dp[-1]
