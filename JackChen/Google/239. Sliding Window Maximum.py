class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        "Deques have O(1) speed for appendleft() and popleft() while lists have O(n) performance for insert(0, value) and pop(0).


        window = []
        ans = []
        for i, n in enumerate(nums):
            while window and nums[window[-1]] < n:
                window.pop()
            window += [i]
            if window[0] == i-k:
                window.pop(0)
            if i >= k - 1:
                ans += [nums[window[0]]]
        return ans


s = Solution()
s.maxSlidingWindow([1],1)
