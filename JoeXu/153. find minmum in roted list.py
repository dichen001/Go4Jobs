class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right and nums[right]<nums[left]:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]