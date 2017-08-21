"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # recursive O(26*N)
        C = collections.Counter(s)
        min_id = 0
        for i, c in enumerate(s):
            if c < s[min_id]:
                min_id = i
            C[c] -= 1
            if C[c] == 0:
                break
        return s[min_id] + self.removeDuplicateLetters(s[min_id+1:].replace(s[min_id], "")) if len(s) != 0 else ""

        # iterative O(26*N)
        ans = []
        while s != "":
            min_id = 0
            C = collections.Counter(s)
            for i, c in enumerate(s):
                if c < s[min_id]:
                    min_id = i
                C[c] -= 1
                if C[c] == 0:
                    break
            ans += [s[min_id]]
            s = s[min_id+1:].replace(s[min_id], "")
        return "".join(ans)

