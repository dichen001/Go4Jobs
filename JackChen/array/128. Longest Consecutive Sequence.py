"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem, result = {}, 0
        for n in nums:
            if not mem.get(n):
                left = mem.get(n-1,0)
                right = mem.get(n+1,0)
                sum = left + right + 1
                mem[n] = sum
                result = max(result, sum)

                mem[n-left] = sum
                mem[n+right] = sum
        return result


    # another NB solusion withou O(1) space
    # Could be understand easily when walking through a small example.  Worst case time is 2*n

class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:       # This line is so smart!
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best
