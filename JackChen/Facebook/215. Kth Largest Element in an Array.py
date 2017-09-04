"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(nums, low, high):
            i = low
            while i < high:
                if nums[i] > nums[high]:
                    nums[i], nums[low] = nums[low], nums[i]
                    low += 1
                i += 1
            nums[high], nums[low] = nums[low], nums[high]
            return low

        random.shuffle(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = partition(nums, l, r)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1