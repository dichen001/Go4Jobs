"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

"""

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        def mergesort(l, r):
            m = (l + r) / 2
            if m == l:
                return 0
            count = mergesort(l, m) + mergesort(m, r)
            i = j = m
            for left in sums[l:m]:
                while i < r and sums[i] - left < lower:
                    i += 1
                while j < r and sums[j] - left <= upper:
                    j += 1
                count += j - i
            sums[l:r] = sorted(sums[l:r])
            return count
        return mergesort(0, len(nums) + 1)