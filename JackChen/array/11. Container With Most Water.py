"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, h, r = 0, len(height)-1, 0
        while l < h:
            r = max(r, (h-l) * min(height[l], height[h]))
            if height[l] < height[h]:
                while l+1 < h and height[l+1] <= height[l]:
                    l += 1
                l += 1
            else:
                while l < h-1 and height[h-1] <= height[h]:
                    h -= 1
                h -= 1
        return r
