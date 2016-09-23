"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        t = len(digits) - 1
        while t >= 0 and digits[t] == 9:
            digits[t] = 0
            t -= 1
        if t < 0:
            digits.insert(0,1)
        else:
            digits[t] += 1
        return digits
