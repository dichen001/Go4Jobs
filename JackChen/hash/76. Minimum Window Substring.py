"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        flag = False
        for c in t:
            need[c] = need[c] + 1 if need.get(c) else 1
        missing = len(t)
        i, start, end = 0, 0, 0
        for j, c in enumerate(s):
            if need.get(c) > 0:
                missing -= 1
            need[c] = need[c] - 1 if need.get(c) else -1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not flag or j - i <= end - start:
                    start, end = i, j
                    flag = True
        return s[start: end + 1] if flag else ''


        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        ## Start from 1 is very important here. think about input "a" "aa"
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
                    print s[I:J]
        return s[I:J]

s = Solution()
s.minWindow("ab", "a")
