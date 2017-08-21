"""
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        we use `max_ave` to denote the maximum average value.
        Then, for any i, j (j-i>=k-1), we can have
            (nums[i] - max_ave) + (nums[i+1] - max_ave)+...+ (nums[j] - max_ave) <= 0.
        Therefore, for some i, j (j-i>=k-1), if we find
            (nums[i] - mid) + (nums[i+1] - mid)+...+ (nums[j] - mid) > 0,
        then mid must be smaller than max_ave.
        """

        ## Works for C, but TLE for Python.

        def is_larger(mid):
            # note that pre_min should be init as 0,
            # meaning when no value before [0:k-1], total should > 0
            total, pre_total, pre_min = 0, 0, 0
            for i in range(len(nums)):
                total += nums[i] - mid
                if i >= k:
                    pre_total += nums[i-k] - mid
                    pre_min = min(pre_min, pre_total)
                if i >= k - 1 and total - pre_min > 0:
                    return False
            return True

        l, r, mid = min(nums), max(nums), nums[0]
        while r - l > 0.000001:
            mid = (l + r) * 0.5
            if is_larger(mid):  r = mid
            else:  l = mid
        return l









s = Solution()
s.findMaxAverage([4,0,4,3,3], 5)
