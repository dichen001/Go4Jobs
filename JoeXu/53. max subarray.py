class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        sum=0
        min=0
        max=nums[0]
        for x in nums:
            sum+=x
            if sum - min>max:
                max=sum-min
            if sum<min:
                min=sum
        return max