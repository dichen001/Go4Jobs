"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)  # This is step is very important.
        result, stack, n = 0, [], len(heights)
        for i in range(n):
            h = heights[i]
            while stack and h <= heights[stack[-1]]:
                hh = heights[stack.pop()]
                left = stack[-1] if stack else -1
                result = max(result, (i - left - 1) * hh)
            stack.append(i)
        return result
