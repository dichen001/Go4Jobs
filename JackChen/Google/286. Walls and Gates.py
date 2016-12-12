"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        infinity = 2147483647
        m, n = len(rooms), len(rooms[0])
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            ij = q.pop(0)
            for d in directions:
                i, j = ij[0], ij[1]
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == infinity:
                    rooms[ni][nj] = rooms[i][j] + 1
                    q.append((ni,nj))




        # first implementation. naive bfs, could be improved much better
        # this one let each empty expand all over the map and update later if bigger
        # while we could let all the empty node expand together
        # if not rooms or not rooms[0]:
        #     return
        # directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # infinity = 2147483647
        # def bfs(rooms, i, j):
        #     q = [(i,j)]
        #     m, n = len(rooms), len(rooms[0])
        #     while q:
        #         ij = q.pop(0)
        #         for d in directions:
        #             i, j = ij[0], ij[1]
        #             ni, nj = i + d[0], j + d[1]
        #             if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] > rooms[ij[0]][ij[1]]:
        #                 rooms[ni][nj] = min(rooms[ni][nj], rooms[i][j] + 1)
        #                 q.append((ni,nj))

        # m, n = len(rooms), len(rooms[0])
        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == 0:
        #             bfs(rooms, i, j)

s = Solution()
s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
