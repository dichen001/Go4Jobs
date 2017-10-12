class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        # note that they cannot reuse integers!!!
        def dfs(nums, left):
            key = str(nums)
            if key in visited:
                return visited[key]
            if nums[-1] >= desiredTotal:
                visited[key] = True
                return True
            for i in range(len(nums)):
                if not dfs(nums[:i] + nums[i + 1:], left - nums[i]):
                    visited[key] = True
                    return True
            visited[key] = False
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        visited = {}
        return dfs(range(1, maxChoosableInteger + 1), desiredTotal)


s = Solution()

print s.canIWin(10, 11)