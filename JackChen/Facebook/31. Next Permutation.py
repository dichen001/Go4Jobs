"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        nums[i:] = nums[i:][::-1]
        if i - 1 > -1:
            # 1342 -> 1324 --> (1423)
            j = i
            while j < len(nums) and nums[j] <= nums[i - 1]:
                j += 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

