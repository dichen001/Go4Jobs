"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words, d1, d2 = str.split(' '), {}, {}
        if len(pattern) != len(words):
            return False
        for i, p in enumerate(pattern):
            if not d1.get(p) and not d2.get(words[i]):
                d1[p], d2[words[i]] = words[i], p
            elif d1.get(p) != words[i] or d2.get(words[i]) != p:
                return False
        return True
