class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
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
print s.numIslands([list(row) for row in ["11000","11000","00100","00011"]])
