class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        head = range(n)
        for e in edges:
            n1, n2 = e[0], e[1]
            while head[n1] != n1:
                n1 = head[n1]
            while head[n2] != n2:
                n2 = head[n2]
            if n1 == n2:
                return False
            head[n2] = n1
        return len(edges) == n-1


        if n-1 != len(edges):
            return False
        if not edges:
            return True
        dic = collections.defaultdict(set)
        for e in edges:
            dic[e[0]].add(e[1])
            dic[e[1]].add(e[0])
        stack, visited = edges[0][:], set()
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for next in dic.get(node, []):
                    stack.append(next)
        return len(visited) == n
