import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        " build tree with BFS and record heigh "

        # build graph first
        graph = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            in_degree[i] += 1
            in_degree[j] += 1

        # build tree: BFS
        queue = [i for i in in_degree.iterkeys() if in_degree[i] == 1]
        height, mem = -1, collections.defaultdict(list)
        while queue:
            height += 1
            size = len(queue)
            for _ in range(size):
                i = queue.pop(0)
                mem[height] += [i]
                for j in graph[i]:
                    in_degree[j] -= 1
                    if in_degree[j] == 1:
                        queue.append(j)
        # 0: 0
        # 1: 1
        # 2: 1
        # 3: 1, 2
        # 4: 2
        # 5: 2,3
        return mem[(height+1)/2] if height < 2 or height % 2 == 0 else mem[(height+1)/2] + mem[(height+1)/2 - 1]


s = Solution()
s.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])