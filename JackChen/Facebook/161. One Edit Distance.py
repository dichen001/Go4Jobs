class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Simplized
        for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            return s[i + (1 if len(s) >= len(t) else 0):] == t[i + (1 if len(s) <= len(t) else 0):]
        return abs(len(s) - len(t)) == 1

        diff = -1
        if abs(len(s) - len(t)) < 2:
            i, count, n = 0, 0, min(len(s), len(t))
            while i < n:
                count += s[i] != t[i]
                diff = i if diff == -1 and s[i] != t[i] else diff
                i += 1
            count += len(s[i:]) + len(t[i:])
            return count == 1 or (diff != -1 and (s[:diff] + s[diff+1:] == t or s == t[:diff] + t[diff+1:]))
        return False
