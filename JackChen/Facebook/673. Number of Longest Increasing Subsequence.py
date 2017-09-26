from bisect import bisect_left
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lengths = counts = [1] * len(nums)
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
            max_len = max(max_len, lengths[i])
        return sum([counts[i] for i in range(len(nums)) if lengths[i] == max_len])

s = Solution()
s.findNumberOfLIS([1,2,4,3,5,4,7,2])