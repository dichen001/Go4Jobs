"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if only need to find any peak
        def bs(l, r):
            if l == r:
                return l
            m1 = (l+r) / 2
            m2 = m1 + 1
            return bs(l, m1) if nums[m1] > nums[m2] else bs(m2, r)

        return bs(0, len(nums) - 1)



        # if we need to find the top peak: O(N)
        ans, nums = 0, [float("-inf")] + nums + [float("-inf")]
        for i, n in enumerate(nums[1:-1], 1):
            if nums[i-1] < nums[i] > nums[i+1] and nums[i] > nums[ans]:
                ans = i
        return ans - 1
