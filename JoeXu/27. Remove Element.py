class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:# create a copy
            #modify nums
            if i==val:
                nums.remove(val)
        l=len(nums)
        return l