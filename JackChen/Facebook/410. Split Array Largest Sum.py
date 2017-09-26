"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
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
        # Binary Search (faster)
        l, r = max(nums), sum(nums)
        if m == 1:
            return r
        while l < r:
            mid = (l + r) / 2
            if self.isValid(nums, m, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def isValid(self, nums, m, mid):
        total, count = 0, 1
        for n in nums:
            total += n
            if total > mid:
                total = n
                count += 1
                if count > m:
                    return False
        return True

        # DP O(N^2)
        N = len(nums)
        accu = [0]
        for n in nums:
            accu += [accu[-1] + n]

        dp = [accu[N] - accu[i] for i in range(N)]

        for l in range(1, m):
            for i in range(N - l):
                dp[i] = accu[-1]
                for j in range(i + 1, N - l + 1):
                    tmp = max(dp[j], accu[j] - accu[i])
                    if tmp <= dp[i]:
                        dp[i] = tmp
                    else:
                        break
        return dp[0]
