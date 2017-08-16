# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         def dfs(i, j):
#             if mem[i][j]:
#                 return mem[i][j]
#             longest = 1
#             for p in [(0,1),(0,-1),(1,0),(-1,0)]:
#                 ni, nj = i + p[0], j + p[1]
#                 if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
#                     longest = max(longest, 1 + dfs(ni, nj))
#             mem[i][j] = longest
#             return longest
#
#         if not matrix or not matrix[0]:
#             return 0
#         m, n = len(matrix), len(matrix[0])
#         mem = [[0] * n for _ in range(m)]
#         result = 0
#         for i in range(m):
#             for j in range(n):
#                 result = max(result, dfs(i,j))
#         return result

# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#
#         def dfs(i, j):
#             if visited[i][j] != 0:
#                 return visited[i][j]
#             visited[i][j] = 1
#             for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < m and 0 <= nj < n and matrix[i][j] >= matrix[ni][nj]:
#                     visited[i][j] = max(visited[i][j], 1 + dfs(ni, nj))
#             return visited[i][j]
#
#         if not matrix or not matrix[0]:
#             return 0
#         m, n = len(matrix), len(matrix[0])
#         ans, visited = 0, [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 ans = max(ans, dfs(i, j))
#         return ans

# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#
#         def dfs(i, j):
#             if visited[i][j] != 0:
#                 return visited[i][j]
#             visited[i][j] = 1
#             track.add((i, j))
#             for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < m and 0 <= nj < n and matrix[i][j] >= matrix[ni][nj] and visited[ni][nj] == 0:
#                     visited[i][j] = max(visited[i][j], 1 + dfs(ni, nj))
#             return visited[i][j]
#
#         if not matrix or not matrix[0]:
#             return 0
#         m, n = len(matrix), len(matrix[0])
#         ans, visited = 0, [[0] * n for _ in range(m)]
#         track = {}
#         for i in range(m):
#             for j in range(n):
#                 tmp_max = dfs(i, j)
#                 ans = max(ans, tmp_max)
#         return ans


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def update(tmp_max):
            for i, j in track:
                visited[i][j] = tmp_max

        def dfs(i, j):
            if visited[i][j] != 0:
                return visited[i][j]
            visited[i][j] = 1
            track.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[i][j] >= matrix[ni][nj] and visited[ni][nj] == 0:
                    visited[i][j] = max(visited[i][j], 1 + dfs(ni, nj))
            return visited[i][j]

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans, visited = 0, [[0] * n for _ in range(m)]
        track = set()
        for i in range(m):
            for j in range(n):
                tmp_max = dfs(i, j)
                ans = max(ans, tmp_max)
                update(tmp_max)
                track = set()
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


s = Solution()
s.longestIncreasingPath([[5,5,5,5,5],[5,5,5,5,5],[5,5,4,4,4],[5,5,5,5,5],[5,5,5,5,5]])
