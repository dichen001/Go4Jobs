# """
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
#
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
# """
#
# class Solution(object):
#
#     def shortestDistance(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         if not grid or not grid[0]:
#             return -1
#         shortest, walk = float('inf'), 0
#         m, n = len(grid), len(grid[0])
#         dist = [[0] * n for _ in range(m)]
#
#         def bfs(i, j, grid, dist, walk):
#             options = [[0,1], [0,-1], [1,0], [-1,0]]
#             m, n = len(grid), len(grid[0])
#             shortest = float('inf')
#             q = [(i,j)]
#             level = 0
#             while q:
#                 level += 1
#                 level_size = len(q)
#                 for ls in range(level_size):
#                     ij = q.pop(0)
#                     for k in range(4):
#                         ni = ij[0] + options[k][0]
#                         nj = ij[1] + options[k][1]
#                         if ni > -1 and ni < m and nj > -1 and nj < n and grid[ni][nj] == walk:
#                             grid[ni][nj] -= 1
#                             q.append((ni,nj))
#                             dist[ni][nj] += level
#                             shortest = min(shortest, dist[ni][nj])
#             return shortest
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     shortest = bfs(i, j, grid, dist, walk)
#                     walk -= 1
#         return shortest if shortest != float('inf') else -1
#
#
#


import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i, j, empty_mark):
            level = 0
            queue = collections.deque([(i,j)])
            while queue:
                level += 1
                count = len(queue)
                for _ in range(count):
                    i, j = queue.popleft()
                    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == empty_mark:
                            grid[ni][nj] = empty_mark - 1
                            dist[ni][nj] += level
                            queue.append((ni,nj))


        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] in [1,2]:
                    dist[i][j] = float('inf')
        empty_mark = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j, empty_mark)
                    empty_mark -= 1
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                ans = min(ans, dist[i][j])
        return ans

s = Solution()
s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])