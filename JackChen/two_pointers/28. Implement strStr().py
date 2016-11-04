class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        start, l1, l2 = 0, len(haystack), len(needle)
        while start < l1:
            if start < l1 and start + l2 - 1 < l1 and haystack[start: start + l2] == needle:
                return start
            start += 1
        return -1

