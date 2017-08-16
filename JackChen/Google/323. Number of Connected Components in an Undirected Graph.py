"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges
"""


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        vertexes = Union(n)
        for e in edges:
            vertexes.union(e[0], e[1])
        return vertexes.count


class Union(object):
    def __init__(self, n):
        self.root, self.size = {}, {}
        for i in range(n):
            self.root[i] = i
            self.size[i] = 1
        self.count = n

    def union(self, p, np):
        proot = self.find(p)
        nproot = self.find(np)
        if proot == nproot:
            return
        if self.size[nproot] > self.size[proot]:
            proot, nproot = nproot, proot
        self.root[nproot] = proot
        self.size[proot] += self.size[nproot]
        self.count -= 1

    def find(self, p):
        if self.root[p] == p:
            return p
        while p != self.root[p]:
            self.root[p] = self.root[self.root[p]]
            p = self.root[p]
        return p