import collections
from heapq import *
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        fromTo = collections.defaultdict(list)
        for t in sorted(tickets)[::-1]:
            fromTo[t[0]] += [t[1]]
        ans = []
        stack = ['JFK']
        while stack:
            while fromTo[stack[-1]] != []:
                stack += fromTo[stack[-1]].pop()
            ans += [stack.pop()]
        return ans[::-1]




s = Solution()
s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
