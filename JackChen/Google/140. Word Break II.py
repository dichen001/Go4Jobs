class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # build Trie       50~70ms
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
                    mem[w] += [w[:i + 1] + " " + p if p != "" else w[:i + 1] for p in dfs(w[i + 1:])]
            return mem[w]

        mem = collections.defaultdict(list)
        mem[""] = [""]
        dfs(s)
        return mem[s]

        # dfs with mem  200~300 ms
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

        # dp (bottom to top) TEL  O(N^2)
        n = len(s)
        dp, words = [[] for _ in range(n + 1)], set(wordDict)
        dp[n] = [""]
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):
                if s[start:end] in words and dp[end] != []:
                    for subs in dp[end]:
                        dp[start] += [s[start:end] + " " + subs] if subs != "" else [s[start:end]]
        return dp[0]

        # dp (left to right) TLE O(N^2)
        dp, words = [['']] + [[] for _ in range(len(s))], set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if len(dp[j]) != 0 and s[j:i] in words:
                    for subs in dp[j]:
                        dp[i] += [subs + " " + s[j:i]] if subs != "" else [s[j:i]]
        return dp[len(s)]


s = Solution()
s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])