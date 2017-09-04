import collections
from heapq import *
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # build graph
        graph = collections.defaultdict(list)
        for s, e in sorted(tickets):
            graph[s] += [e]

        # dfs
        def dfs(s):
            if not s:
                return
            while graph[s]:
                dfs(graph[s].pop(0))
            ans.append(s)
            return False

        ans = []
        dfs("JFK")
        return ans[::-1]



s = Solution()
s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
