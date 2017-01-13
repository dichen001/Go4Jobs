class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_tails = [0] * len(nums)
        size = 0
        for n in nums:
            left, right = 0, size
            # left = bisect.bisect_left(min_tails, n, left, right)
            # # bisect.insort(min_tails, n, left, right)
            while left != right:
                m = (left + right) / 2
                if min_tails[m] < n:
                    left = m + 1
                else:
                    right = m
            min_tails[left] = n
            size = max(size, left + 1)
        return size

s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 1])
