import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        " build tree with BFS and record heigh "
        if not edges:
            return [0]
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
        return mem[height]


s = Solution()
print s.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])