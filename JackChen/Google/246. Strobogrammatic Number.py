"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        valids = {'0','1','6','8','9'}
        updown = []
        for n in num:
            if str(n) not in valids:
                return False
            elif n == '6':
                updown.append('9')
            elif n == '9':
                updown.append('6')
            else:
                updown.append(n)
        return num == ''.join(updown[::-1])
