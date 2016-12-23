"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

## Need to realize that if A~B = C, then A~C = B and B~C = A. A, B and C are all 32 bits.


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {n >> i for n in nums}
            for p in prefixes:
                if (ans ^ 1 ^ p) in prefixes:
                    ans ^= 1
                    break
        return ans


        max, mask = 0, 0
        for i in range(32)[::-1]:
            mask |= 1 << i
            prefixes = {num & mask for num in nums}
            tmp = max | (1 << i)
            for p in prefixes:
                if (tmp ^ p) in prefixes:
                    max = tmp
                    break
        return max
