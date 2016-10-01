"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums)<1 or (len(nums)==1 and target != nums[0]):
            return -1
        mid = (len(nums)-1)/2
        if target == nums[mid]:
            return mid
        # right side is sorted
        if nums[mid] < nums[-1]:
            if target > nums[mid]:
                return mid + 1 + self.search(nums[mid+1:], target) if self.search(nums[mid+1:], target)!=-1 else -1
            else:
                return self.search(nums[:mid+1], target)
        # left side is sorted
        else:
            if target <= nums[mid]:
                return self.search(nums[:mid+1], target)
            else:
                return mid + self.search(nums[mid+1:], target) if self.search(nums[mid+1:], target)!=-1 else -1




s = Solution()
s.search([3,1], 1)
