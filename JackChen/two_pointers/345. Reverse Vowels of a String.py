"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [c for c in s]
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        while l < r:
            while s[l].lower() not in vowels and l < r:
                l += 1
            while s[r].lower() not in vowels and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        return ''.join(s)


s = Solution()
s.reverseVowels('hello')
