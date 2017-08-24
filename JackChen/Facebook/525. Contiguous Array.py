"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem, count, ans = {0: -1}, 0, 0
        for i, n in enumerate(nums):
            count += 1 if n else -1
            if count in mem:
                ans = max(ans, i - mem[count])
            else:
                mem[count] = i
        return ans


s = Solution()
s.findMaxLength([0,0,1,0,0,0,1,1])
