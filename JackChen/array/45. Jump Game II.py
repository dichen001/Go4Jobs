"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        step, next = 0, 0
        while next < n - 1:
            step += 1
            if next + nums[next] >= n - 1:
                return step
            this_ranges = range(next, next + nums[next] + 1)
            next_ranges = [i + nums[i] for i in this_ranges]
            furthest = max(next_ranges)
            next = next + next_ranges.index(furthest)
        return step

s = Solution()
print s.jump([5,9,3,2,1,0,2,3,3,1,0,0])
