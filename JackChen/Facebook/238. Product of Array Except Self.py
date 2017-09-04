"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(N) time, O(1) space.
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] = ans[i - 1] * nums[i]
        after, ans[-1], = nums[-1], ans[-2]
        for i in range(n - 2, 0, -1):
            ans[i] = ans[i - 1] * after
            after *= nums[i]
        ans[0] = after
        return ans

        # O(N) time, O(N) space.
        n = len(nums)
        pre, after = [1] * n, [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]
        ans = []
        for i in range(n):
            ans.append(pre[i] * after[i])
        return ans