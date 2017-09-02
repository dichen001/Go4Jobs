"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # O(N * M^2) where N = number of words, M = len(word)
        ans = []
        mem = {w: i for i, w in enumerate(words)}
        for i, w in enumerate(words):
            for k in range(len(w) + 1):

                l, r = w[:k], w[k:]
                l_rev, r_rev = l[::-1], r[::-1]
                if l == l_rev and r_rev in mem and mem[r_rev] != i:
                    ans.append([mem[r_rev], i])
                if len(r) != 0 and r == r_rev and l_rev in mem and mem[l_rev] != i:
                    ans.append([i, mem[l_rev]])
        return ans




        ans, mem = [], {w: i for i, w in enumerate(words)}
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                l, r = w[:j], w[j:]
                l_rev, r_rev = l[::-1], r[::-1]
                if r == r_rev and l_rev in mem and mem[l_rev] != i:
                    ans.append([i, mem[l_rev]])
                if j != 0 and l == l_rev and r_rev in mem and mem[r_rev] != i:
                    ans.append([mem[r_rev], i])
        return ans