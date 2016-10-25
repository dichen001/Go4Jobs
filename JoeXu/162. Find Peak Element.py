class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<=1:
            return 0
        elif l==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        else:
            for i in range(1,l-1):
                if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                    return i
        return [0,l-1][nums[0]<nums[l-1]]