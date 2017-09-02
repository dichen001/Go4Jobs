"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        C = collections.Counter(s)
        odd = 0
        for c, cnt in C.iteritems():
            if cnt % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True