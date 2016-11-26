"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 1 ≤ m ≤ length(nums) ≤ 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def dividable(nums, limit, total_cut):
            accu, cut = 0, 1
            for n in nums:
                if accu + n <= limit:
                    accu += n
                else:
                    cut += 1
                    accu = n
                    if cut > total_cut:
                        return False
            return True

        biggest, sum = float('-inf'), 0
        for n in nums:
            sum += n
            biggest = max(biggest, n)
        l, r = biggest, sum
        while l < r:
            mid = (l + r) / 2
            if dividable(nums, mid, m):
                r = mid
            else:
                l = mid + 1
        return l

