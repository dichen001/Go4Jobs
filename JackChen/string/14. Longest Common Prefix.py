"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(str1, str2):
            i, l = 0, min(len(str1), len(str2))
            while i < l:
                if str1[i] == str2[i]:
                    i = i+1
                else:
                    break
            return str1[:i]
        return reduce(lcp, strs) if strs else ''
