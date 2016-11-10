"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r = 0, n - 1
        l_max, r_max = 0, 0
        result = 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    result += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    result += r_max - height[r]
                r -= 1
        return result
