"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        """
        n = len(num)
        if n == k:
            return "0"
        min = num[:n-k]
        for new_digit in num[n-k:]:
            tmp_min = min
            for i in range(len(min)):
                tmp = list(min)
                tmp.__delitem__(i)
                tmp.append(new_digit)
                if int(''.join(tmp)) < int(tmp_min):
                    tmp_min = ''.join(tmp)
            if int(tmp_min) < int(min):
                min = tmp_min
        return str(int(min))
        """
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        return ''.join(stack[:-k or None]).lstrip('0') or '0'


s = Solution()
s.removeKdigits('1432219', 3)