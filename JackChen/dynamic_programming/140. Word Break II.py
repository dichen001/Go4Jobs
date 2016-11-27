class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [[False, set()] for _ in range(n+1)]
        dp[0] = [True, {0}]
        for j in range(1, n+1):
            for i in range(j):
                if dp[i][0] and s[i:j] in wordDict:
                    dp[j][0] = True
                    dp[j][1].add(i)
        result = []
        starts = dp[n][1]
        end = n
        def backtrack(starts, end, path):
            if end <= 0:
                result.append(' '.join(path[::-1]))
                return
            for start in starts:
                word = s[start:end]
                path_update = path + [word]
                backtrack(dp[start][1], start, path_update)
        backtrack(starts, end, [])
        return result




s = Solution()
s.wordBreak("catsanddogsand", set(["cat","cats","and","sand","dog", "dogs"]))
