"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
"""

from random import shuffle
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, low, high):
            pivot = nums[high]
            l = low
            while l < high:
                if nums[l] > nums[high]:
                    nums[l], nums[low] = nums[low], nums[l]
                    low += 1
                l += 1
            nums[high], nums[low] = nums[low], nums[high]
            return low

        def partition_2(nums, low, high):
            pivot = nums[high]
            l, r = low, high - 1
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                    l, r = l + 1, r - 1
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[l], nums[high] = nums[high], nums[l]
            return l

        shuffle(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = partition(nums, left, right)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                left = pivot + 1
            else:
                right = pivot - 1



s = Solution()
print s.findKthLargest([99,99],1)
