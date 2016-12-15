class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i,j):
            if mem[i][j]:
                return mem[i][j]
            if i == 0 or j == 0:
                mem[i][j].add(1)
            if i == m-1 or j == n-1:
                mem[i][j].add(2)
            # mark as visited
            mem[i][j] = mem[i][j].union({0})
            for p in [(0,-1),(-1,0),(1,0),(0,1)]:
                ni, nj = i + p[0], j + p[1]
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] <= matrix[i][j]:
                    print str(i) + ' ' +  str(j) + '\t-->\t' + str(ni) + ' ' +  str(nj)
                    mem[i][j] = mem[i][j].union(dfs(ni, nj))

            if 1 in mem[i][j] and 2 in mem[i][j]:
                result.append([i,j])
            return mem[i][j]

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        mem = [[set() for _ in range(n)] for _ in range(m)]
        result = []
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        return result
        #
        #
        # def dfs(i, j, k, pre):
        #     if i < 0 or i >= m or j < 0 or j >= n or visited[i][j][k] or matrix[i][j] < pre:
        #         return
        #     visited[i][j][k] = 1
        #     for p in [(0,1), (0,-1), (1,0), (-1,0)]:
        #         ni, nj = i+p[0], j+p[1]
        #         dfs(ni, nj, k, matrix[i][j])
        #     if visited[i][j][0] and visited[i][j][1]:
        #         ans.append([i,j])
        #
        # if not matrix or not matrix[0]:
        #     return []
        # ans = []
        # m , n = len(matrix), len(matrix[0])
        # visited = [[[0,0] for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     dfs(i, 0, 0, float('-inf'))
        #     dfs(i, n-1, 1, float('-inf'))
        # for j in range(n):
        #     dfs(0, j, 0, float('-inf'))
        #     dfs(m-1, j, 1, float('-inf'))
        #
        # return ans

s = Solution()
s.pacificAtlantic([[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]])
