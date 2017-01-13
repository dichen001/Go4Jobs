import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        ## BFS
        # build graph
        graph = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        all_nodes = set()
        for seq in seqs:
            for i in range(len(seq)):
                all_nodes |= {seq[i]}
                if i == 0:
                    in_degree[seq[i]] += 0
                if i < len(seq) - 1 and seq[i+1] not in graph[seq[i]]:
                    graph[seq[i]].add(seq[i+1])
                    in_degree[seq[i+1]] += 1
        n = len(org)
        if len(all_nodes) != n:
            return False
        queue = [i for i in range(1,n+1) if in_degree[i] == 0]
        reconstruct = []
        while len(queue) == 1:
            i = queue.pop()
            reconstruct += [i]
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
        return len(queue) == 0 and reconstruct == org
        
s = Solution()
print s.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])