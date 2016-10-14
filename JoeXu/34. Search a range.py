class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        left=0
        right=l-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                res=[0,0]
                if nums[left]==target:
                    res[0]=left
                if nums[right]==target:
                    res[1]=right
                for i in range(mid,right+1):
                    if nums[i]!=target:
                        res[1]=i-1
                        break
                for i in range(mid,left-1,-1):
                    if nums[i]!=target:
                        res[0]=i+1
                        break
                return res
        return [-1,-1]    
                    