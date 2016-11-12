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
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        ## O(n*k) Solution, where k is the max length of word in words.
        results, mem, n = [], {}, len(words)
        for i in range(n):
            mem[words[i]] = i
        for i in range(n):
            for j in range(len(words[i])+1):
                l, r = words[i][0:j], words[i][j:]
                l_rev, r_rev = l[::-1], r[::-1]
                if mem.get(l_rev, -1) >= 0 and mem[l_rev] != i and isPalindrome(r):
                    results.append([i, mem[l_rev]])
                if j>0 and mem.get(r_rev, -1) >= 0 and mem[r_rev] != i and isPalindrome(l):
                    results.append([mem[r_rev], i])
        return results

        ## O(n^2) Solution
        results = []
        for i, wi in enumerate(words[:-1]):
            for j, wj in enumerate(words[i+1:]):
                wij, wji, l = wi + wj, wj + wi, len(wi) + len(wj)
                mid_l, mid_r = l / 2, (l+1) / 2
                if wij[:mid_l] == wij[mid_r:][::-1]:
                    results.append([i,i+j+1])
                if wji[:mid_l] == wji[mid_r:][::-1]:
                    results.append([i+j+1,i])
        return results


s = Solution()
print s.palindromePairs(["a","b","c","ab","ac","aa"])
