"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # O(Nlog(N))
        self.n = len(nums)
        self.nums = [0] * self.n
        self.BIT = [0] * (self.n + 1)
        for i, n in enumerate(nums):
            self.update(i, n)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < self.n + 1:
            self.BIT[i] += diff
            i += i & -i


    def getSum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.BIT[i]
            i -= i & -i
        return ret


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j) - self.getSum(i-1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
