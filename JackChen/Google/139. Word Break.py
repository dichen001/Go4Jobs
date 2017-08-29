"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp  slower but shorter
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for l in range(1, n + 1):
            for j in range(l):
                if dp[j] and s[j:l] in wordDict:
                    dp[l] = True
                    break
        return dp[n]

        # Trie  faster but longer
        root = {}
        for w in wordDict:
            node = root
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["end"] = w

        def dfs(w):
            if w in mem:
                return mem[w]
            node = root
            for i, c in enumerate(w):
                if c not in node:
                    break
                node = node[c]
                if "end" in node:
                    mem[w] = mem.get(w, False) or dfs(w[i + 1:])
            return mem.get(w, False)

        mem = {"": True}
        dfs(s)
        return mem.get(s, False)
