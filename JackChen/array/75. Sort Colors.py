"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        color = {0:0,1:0,2:0}
        for n in nums:
            color[n] += 1
        i = 0
        for c in color:
            while color[c] > 0:
                nums[i] = c
                color[c] -= 1
                i += 1
