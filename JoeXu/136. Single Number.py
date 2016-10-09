class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        for i in range(1,len(nums)):
            temp = temp ^ nums[i]
        return temp