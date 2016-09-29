"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return list(set(nums))
        r1, r2, c1, c2 = 0, 0, 0, 0
        for n in nums:
            if n == r1:
                c1 += 1
            elif n == r2:
                c2 += 1
            elif c1 == 0:
                r1, c1 = n, 1
            elif c2 == 0:
                r2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        return [i for i in set(nums) if nums.count(i) > len(nums)//3 ]




