import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ans, graph, indegree = 0, {}, {}
        for a, b in prerequisites:
            graph[a] = graph.get(a, []) + [b]
            indegree[b] = indegree.get(b, 0) + 1
        queue = collections.deque([i for i in range(numCourses) if i not in indegree])
        while queue:
            t = queue.popleft()
            ans += 1
            for take in graph.get(t, []):
                indegree[take] -= 1
                if indegree[take] == 0:
                    queue += [take]
        return ans == numCourses


        "BFS Solution: Keep track of in_degree"
        # build graph
        graph = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        for i, j in prerequisites:
            # in case of repeative i,j will make the in_degree wrong
            if i not in graph[j]:
                in_degree[i] += 1
                graph[j].add(i)
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        count = len(queue)
        while queue:
            i = queue.pop(0)
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
                    count += 1
        return count == numCourses
            
        
        "DFS Solution, keep track of ondes on current path"
        # dfs return True if circle found
        def dfs_cycle(i, cur):
            if i in visited:
                return False
            visited.add(i)
            cur.add(i)
            for j in graph[i]:
                if j in cur or dfs_cycle(j, cur):
                    return True
            cur.remove(i)
            return False
            
        # build graph
        graph = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[j].add(i)
        
        # find circle
        visited = set()
        for i in range(numCourses):
            if i not in visited:
                if dfs_cycle(i, cur=set()):
                    return False
        return True
        
    
s = Solution()
s.canFinish(2,[[1, 0]])
                    
        
