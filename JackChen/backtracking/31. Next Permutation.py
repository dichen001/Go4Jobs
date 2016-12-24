class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        # find the end of the decending order from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        l, r = i, n-1
        # reverse the decending to acsending order
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        # nums[i-1] is the one need to be sawped with the first one bigger than it in the successing part.
        if i > 0:
            k = i-1
            while nums[k] >= nums[i]:
                i += 1
            nums[i], nums[k] = nums[k], nums[i]


        # n = len(nums)
        # i = n - 1
        #
        # while i > 0 and nums[i-1] >= nums[i]:
        #     i -= 1
        #
        # l, r = i, n - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l+1, r-1
        #
        # if i > 0:
        #     k = i - 1
        #     while nums[i-1] >= nums[k]:
        #         k += 1
        #     nums[i-1], nums[k] = nums[k], nums[i-1]


