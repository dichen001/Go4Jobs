class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def df(start):
            if start in mem:
                return mem[start]
            ret = []
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    rest = df(end)
                    for w in rest:
                        ret += [s[start:end] + ' ' + w] if w != '' else [s[start:end]]
            mem[start] = ret
            return ret

        mem = {len(s): [""]}
        return df(0)


        dp, words = [['']] + [[] for _ in range(len(s))], set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if len(dp[j]) != 0 and s[j:i] in words:
                    for subs in dp[j]:
                        dp[i] += [subs + " " + s[j:i]] if subs != "" else [s[j:i]]
        return dp[len(s)]


s = Solution()
s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])