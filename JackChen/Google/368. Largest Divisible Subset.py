class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return nums
        mem = [0] * n
        nums.sort()
        for i in range(n):
            mem[i] = [nums[i]]
            for j in range(i):
                if nums[i] % mem[j][0] and len(mem[j]) + 1 > len(mem[i]):
                    mem[i] = mem[j] + [nums[i]]
        return mem[n-1]

s = Solution()
s.largestDivisibleSubset([1,2,4])
