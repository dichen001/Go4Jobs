class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        # n = len(A)
        # # this will return the minimum cost start at i.
        # # dp[i] from n-1 to 0, dp[i] = A[i] + dp[i+j] for j in range(1, B+1) if i + j < n and A[i+j] != -1
        # dp = [float("inf"), []] * n
        # dp[n-1] = [A[n-1], [n]]
        # for i in range(n-2, -1, -1):
        #     if A[i] != -1:
        #         for j in range(i+1, i+B+1):
        #             if j < n and A[j] != -1:
        #                 cost = A[i] + dp[j][0]
        #                 if cost < dp[i][0]:
        #                     dp[i][0] = cost
        #                     dp[i][1] = [i+1] + dp[j][1]
        # return dp[0][1]

        # dfs version
        # dfs(i) return the lowest cost and corresponding path start at i
        n = len(A)
        mem = {n-1: [A[n-1], [n]]}
        def dfs(i):
            if i in mem:
                return mem[i]
            local_min, local_path = float('inf'), []
            for j in range(i+1, i+B+1):
                if j < n and A[j] != -1:
                    next_cost, next_path = dfs(j)
                    if next_cost < local_min:
                        local_min = next_cost
                        local_path = next_path
            mem[i] = A[i] + local_min, [i+1] + local_path
            return mem[i]
        return dfs(i=0)[1]


s = Solution()
s.cheapestJump([1,2,4,-1,2], 1)
