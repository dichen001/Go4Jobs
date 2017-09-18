"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def dfs(pattern, s, mem, visited):
            if len(pattern) > len(str):
                return False
            if len(pattern) == 0:
                return True if len(s) == 0 else False
            for i in range(1, len(s) - len(pattern) + 2):
                if pattern[0] not in mem and s[:i] not in visited:
                    mem[pattern[0]] = s[:i]
                    if dfs(pattern[1:], s[i:], mem, visited | {s[:i]}):
                        return True
                    del mem[pattern[0]]
                elif pattern[0] in mem and mem[pattern[0]] == s[:i] \
                        and dfs(pattern[1:], s[i:], mem, visited):
                    return True
            return False

        return dfs(pattern, str, {}, set())