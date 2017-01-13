import collections
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
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
        ans = queue[:]
        while queue:
            i = queue.pop(0)
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
                    ans.append(j)
        return ans if len(ans) == numCourses else []


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
            ans.append(i)
            return False

        # build graph
        graph = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[j].add(i)

        # find circle
        visited = set()
        ans = []
        for i in range(numCourses):
            if i not in visited:
                if dfs_cycle(i, cur=set()):
                    return []
        return ans[::-1]