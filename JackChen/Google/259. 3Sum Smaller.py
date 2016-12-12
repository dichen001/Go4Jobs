"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        if n < 3:
            return 0
        nums.sort()
        for i in range(0, n-2):
            # if i > 0 and nums[i] == nums[i-1]: continue
            l, h = i+1, n-1
            while l < h:
                cur = nums[i] + nums[l] + nums[h]
                if cur < target:
                    ans += h - l
                    l += 1
                else:
                    # while l<h and nums[h-1] == nums[h]: h -= 1
                    h -= 1
        return ans


def outter():
    i = 1
    print 'outer-b'
    print i
    def inner(i):
        i -= 1
        print 'inner'
        print i
    inner(i)
    print 'outer-b'
    print i

outter()
