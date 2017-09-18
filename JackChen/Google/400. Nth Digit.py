"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # optimazed and easy understanding
        for length in range(1, 11):
            start = 10 ** (length - 1)
            if n <= start * 9 * length:
                return int(str(start + (n - 1) / length)[(n - 1) % length])
            n -= start * 9 * length

        # solution 2
        # find the lenth
        length, start, count = 1, 1, 9
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # find the number
        number = str(start + (n - 1) / length)
        return int(number[(n - 1) % length])