class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        l=len(nums)
        while i<l:
            if nums[i]>0 and nums[i]<=l and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i in range(l):
            if nums[i]!=i+1:
                return i+1
        return l+1