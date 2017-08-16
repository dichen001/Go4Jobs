"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
import bisect
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def mergesort(l, r):
            m = (l + r) / 2
            if m == l:
                return 0
            total = mergesort(l, m) + mergesort(m, r)
            for i in range(l, m):
                # j = m
                # while j < r and nums[i] > 2 * nums[j]:
                #     j += 1
                # count += j - m
                target = (nums[i] -1) / 2
                idx = bisect.bisect_right(nums, target, m, r)
                total += idx - m
            nums[l:r] = sorted(nums[l:r])
            return total
        return mergesort(0, len(nums))
