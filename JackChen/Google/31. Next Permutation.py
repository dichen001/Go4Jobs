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
        n = len(nums)
        i = n - 1
        # find the end of the decending order from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # reverse the decending to acsending order
        l, r = i, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        # nums[i-1] is the one need to be sawped with the first one bigger than it in the successing part.
        if i > 0:
            k = i - 1
            while nums[i-1] >= nums[k]:
                k += 1
            nums[i-1], nums[k] = nums[k], nums[i-1]





