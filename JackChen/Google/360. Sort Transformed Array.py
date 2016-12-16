"""
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
"""

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        ans = []
        if a == 0:
            ans = [b*x + c for x in nums]
            return ans if b >=0 else ans[::-1]
        mid = -b/float(2*a)
        left = [n for n in nums if n <= mid]
        right = nums[len(left):]
        while left and right:
            if mid - left[-1] >= right[0] - mid:
                x = right.pop(0)
            else:
                x = left.pop()
            ans.append(a*x*x + b*x + c)
        if left:
            ans += [a*x*x + b*x + c for x in left][::-1]
        if right:
            ans += [a*x*x + b*x + c for x in right]
        return ans if a > 0 else ans[::-1]
