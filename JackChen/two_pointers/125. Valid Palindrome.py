"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(re.findall(r"\w+",s)).lower()
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        return l == r or l == r+1
