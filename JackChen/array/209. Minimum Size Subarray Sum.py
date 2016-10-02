
# CORRECT for finding the minimal length, but NOT the minimal SUB-Arrary!!!
class Solution(object):
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        if nums == [] or sum(nums)<s:
            return 0
        if nums[0] >= s:
            return 1
        result = 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] <= s:
                result += 1
                following = self.minSubArrayLen(s-nums[i], nums[i+1:])
                return result + following
            i += 1
        return result


# excellent solution!s
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, end, sum, min, n = 0, 0, 0,  float("inf"), len(nums)
        while end < n:
            end, sum  = end + 1, sum + nums[end]
            while sum >= s:
                start, sum = start+1, sum - nums[start]
                min = end-start+1 if min > end-start+1 else min
        return min if min != float("inf") else 0


s = Solution()
s.minSubArrayLen(4, [1,4,4])
