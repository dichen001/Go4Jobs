class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i, j, k, pre):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j][k] or matrix[i][j] < pre:
                return
            visited[i][j][k] = 1
            for p in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+p[0], j+p[1]
                dfs(ni, nj, k, matrix[i][j])
            if visited[i][j][0] and visited[i][j][1]:
                ans.append([i,j])

        if not matrix or not matrix[0]:
            return []
        ans = []
        m , n = len(matrix), len(matrix[0])
        visited = [[[0,0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dfs(i, 0, 0, float('-inf'))
            dfs(i, n-1, 1, float('-inf'))
        for j in range(n):
            dfs(0, j, 0, float('-inf'))
            dfs(m-1, j, 1, float('-inf'))

        return ans
