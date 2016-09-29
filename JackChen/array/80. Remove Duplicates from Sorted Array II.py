"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        result, count = 0, 0
        pre = nums[0]
        tmp = nums[:]
        idx = 0
        for i, n in enumerate(tmp):
            if n == pre:
                count += 1
            else:
                pre = n
                count = 1
            if count <= 2:
                result += 1
            else:
                nums.pop(i-idx)
                idx += 1
        return result

def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


s = Solution()
s.removeDuplicates([1,1,1,2,2,3])
