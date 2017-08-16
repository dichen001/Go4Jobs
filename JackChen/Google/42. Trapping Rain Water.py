"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, water = 0, len(height) - 1, 0
        if r < 2:
            return 0
        while l < r:
            if height[l] < height[r]:
                water += max(0, height[l] - height[l+1])
                height[l+1] = max(height[l], height[l+1])
                l += 1
            else:
                water += max(0, height[r] - height[r-1])
                height[r-1] = max(height[r], height[r-1])
                r -= 1
        return water