"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""



import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def bfs(i, j):
            grid[i][j] = 'x'
            queue = collections.deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        grid[ni][nj] = 'x'
                        queue.append((ni, nj))

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        return ans

        def checkSurronding(grid, i,j):
            m, n = len(grid), len(grid[0])
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            q = [(i,j)]
            grid[i][j] = '-1'
            while q:
                size = len(q)
                for k in range(size):
                    ij = q.pop()
                    for d in directions:
                        ni, nj = ij[0]+d[0], ij[1]+d[1]
                        if -1 < ni and ni < m and -1 < nj and nj < n and grid[ni][nj] == '1':
                            grid[ni][nj] = '-1'
                            q.append((ni,nj))

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        # copy = [row.split for row in grid]
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    checkSurronding(grid, i,j)
        return islands



"set"
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def checkSurronding(grid, unvisited, i,j):
            m, n = len(grid), len(grid[0])
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            q = [(i,j)]
            while q:
                size = len(q)
                for k in range(size):
                    ij = q.pop(0)
                    for d in directions:
                        ni, nj = ij[0]+d[0], ij[1]+d[1]
                        if -1 < ni and ni < m and -1 < nj and nj < n and grid[ni][nj] == '1':
                            grid[ni][nj] = '-1'
                            unvisited.remove((ni,nj))
                            q.append((ni,nj))

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        unvisited = set([(i, j) for i in range(m) for j in range(n)])
        islands = 0
        while unvisited:
            ij = unvisited.pop()
            i, j = ij[0], ij[1]
            if grid[i][j] == '1':
                islands += 1
                grid[i][j] = '-1'
                checkSurronding(grid, unvisited, i,j)
        return islands



# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         def checkSurronding(grid, i,j):
#             m, n = len(grid), len(grid[0])
#             directions = [(0,1), (0,-1), (1,0), (-1,0)]
#             unvisited, sea = 0, 0
#             count = 0
#             for d in directions:
#                 ni, nj = i+d[0], j+d[1]
#                 if -1 < ni and ni < m and -1 < nj and nj < n:
#                     count += 1
#                     if grid[ni][nj] == '1':
#                         unvisited += 1
#                     if grid[ni][nj] == '0':
#                         sea += 1
#             # marked as visited
#             grid[i][j] = '-1'
#             if count == sea + unvisited:
#                 return 1
#             return 0
#
#         if not grid or not grid[0]:
#             return 0
#         m, n = len(grid), len(grid[0])
#         # copy = [row.split for row in grid]
#         islands = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     islands += checkSurronding(grid, i,j)
#         return islands


s = Solution()
print s.numIslands([list(row) for row in ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]])
