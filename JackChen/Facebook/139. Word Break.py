import collections
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # build Trie
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
                    mem[w] += [w[:i + 1] + " " + p if p !=  "" else w[:i + 1] for p in dfs(w[i + 1:])]
            return mem[w]

        mem = collections.defaultdict(list)
        mem[""] = [""]
        dfs(s)
        return mem[s]


s = Solution()
s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])