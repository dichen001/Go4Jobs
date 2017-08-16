"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""


class Solution(object):

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                np = (p[0] + d[0], p[1] + d[1])
                if np in islands.roots:
                    islands.union(p, np)
            ans.append(islands.count)
        return ans

# add a size dict saving the size of each Union will help balance the join step. i.e. small join big unions.
class Union(object):
    def __init__(self):
        self.roots = {}
        self.size = {}
        self.count = 0

    def add(self, p):
        self.roots[p] = p
        self.size[p] = 1
        self.count += 1

    def union(self, p, np):
        proot = self.find(p)
        nproot = self.find(np)
        if proot == nproot:
            return
        # optional optimization step.
        if self.size[proot] > self.size[nproot]:
            proot, nproot = nproot, proot
        self.roots[proot] = nproot
        self.size[nproot] += self.size[proot]
        self.count -= 1

    def find(self, p):
        while self.roots[p] != p:
            self.roots[p] = self.roots[self.roots[p]]
            p = self.roots[p]
        return p


