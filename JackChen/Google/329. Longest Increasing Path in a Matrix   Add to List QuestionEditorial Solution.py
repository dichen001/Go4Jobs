class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if mem[i][j]:
                return mem[i][j]
            longest = 1
            for p in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i + p[0], j + p[1]
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    longest = max(longest, 1 + dfs(ni, nj))
            mem[i][j] = longest
            return longest

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        mem = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i,j))
        return result


s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
