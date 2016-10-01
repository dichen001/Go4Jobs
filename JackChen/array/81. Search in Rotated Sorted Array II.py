"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, h = 0, len(nums)-1
        while l<h:
            mid = (l+h)/2
            if target == nums[mid]:
                return True
            # right side is sorted
            if nums[mid] < nums[h]:
                if target > nums[mid] and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
            # left side is sorted
            elif nums[mid] > nums[h]:
                if target >= nums[l] and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                h -= 1
        return target == nums[l]
