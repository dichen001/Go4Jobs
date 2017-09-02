"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # use list instead of dict
        # all use bit manipulation instead of *
        ans = 0
        mask = [0] * len(words)
        for i, w in enumerate(words):
            for c in set(w):
                mask[i] |= 1 << ord(c) - ord("a")
        for i, wi in enumerate(words):
            for j, wj in enumerate(words[i + 1:], i + 1):
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(wi) * len(wj))
        return ans

        # my solution. got TLE when no mem, but get 20% when add mem
        def getMask(w):
            mask = 0
            for c in set(w):
                mask += 2 ** (ord(c) - ord("a"))
            return mask

        n = len(words)
        ans = 0
        mem = {}
        for w in words:
            mem[w] = (getMask(w), len(w))
        for i, wi in enumerate(words):
            # si = mem[wi][0]
            mi = mem[wi][0]
            for j, wj in enumerate(words[i + 1:], i + 1):
                # sj = mem[wj][0]
                mj = mem[wj][0]
                # if not si & sj:
                if mi & mj == 0:
                    ans = max(ans, mem[wi][1] * mem[wj][1])
        return ans








        "previous one"
        n = len(words)
        mask = [0] * n
        for i, w in enumerate(words):
            for c in w:
                mask[i] |= 1 << (ord(c) - ord('a'))
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if not mask[i] & mask[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
