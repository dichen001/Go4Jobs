class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[::-1] + s
        for i in range(len(s))[::-1]:
            l, r = s[:i], s[i:]
            if l == l[::-1]:
                if l != "" and len(r[::-1] + l + r) < len(ans):
                    ans = r[::-1] + l + r
                elif l == "" and len(r) < len(ans):
                    ans = r
        return ans

s = Solution()
s.shortestPalindrome("aacecaaa")