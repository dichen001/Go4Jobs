"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x =
[2, 1, 1, 2]
,
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)
Example 2:
Given x =
[1, 2, 3, 4]
,
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)
Example 3:
Given x =
[1, 1, 1, 1]
,
┌───┐
│   │
└───┼>

Return true (self crossing)
"""

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in xrange(len(x)):
            a, b, c, d, e, f = (x[i:i+6] + [0] * 6)[:6]
            if d >= b >0 and (c <= a or e >= c-a and e <= c and f >= d-b):
                return True
        return False
