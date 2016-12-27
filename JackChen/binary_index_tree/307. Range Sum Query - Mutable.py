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
Hide Tags Segment Tree Binary Indexed Tree
Hide Similar Problems
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        if n <= 0:
            return
        self.n = n
        self.nums = nums
        self.BIT = [0] * (n+1)
        for i, v in enumerate(nums):
            self.update(i,v)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if self.n <= 0:
            return
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.BIT[i] += diff
            i += i & -i

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sum(k):
            r = 0
            while k > 0:
                r += self.BIT[k]
                k -= k & -k
            return r
        return sum(j+1) - sum(i)




# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,3,5])
numArray.sumRange(0, 2)
numArray.update(1, 2)
numArray.sumRange(0, 2)
