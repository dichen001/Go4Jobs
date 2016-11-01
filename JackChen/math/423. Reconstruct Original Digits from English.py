"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def removeWord(word, string, times):
            for c in word:
                string = string.replace(c, '', times)
            return string
        result = []
        insights = ['z', 'w', 'x', 's', 'g', 'v', 'f', 'r', 'o', 'i']
        represents = ['zero', 'two', 'six', 'seven', 'eight', 'five', 'four', 'three', 'one', 'nine']
        numbers = [0, 2, 6, 7, 8, 5, 4, 3, 1, 9]
        while s:
            for i in range(10):
                if insights[i] in s:
                    times = s.count(insights[i])
                    s = removeWord(represents[i], s, times)
                    result += [numbers[i]] * times
        result.sort()
        return ''.join([str(n) for n in result])
                            


s = Solution()
s.originalDigits("owoztneoer")
