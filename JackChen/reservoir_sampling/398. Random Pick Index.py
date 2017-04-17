import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        c = 0
        count = -1
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                if 0 == random.randint(0, count):
                    c = i
        return c



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)