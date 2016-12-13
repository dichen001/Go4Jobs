import heapq
from collections import defaultdict
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        livB, skyline = [], []
        i, n = 0, len(buildings)
        while i<n or livB:
            if not livB or (i<n and -livB[0][1] >= buildings[i][0]):
                x = buildings[i][0]
                while i<n and buildings[i][0] == x:
                    heapq.heappush(livB, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -livB[0][1]
                while livB and -livB[0][1] <= x:
                    heapq.heappop(livB)
            cur_h = -livB[0][0] if livB else 0
            if not skyline or cur_h != skyline[-1][1]:
                skyline.append([x, cur_h])
        return skyline



s = Solution()
s.getSkyline([[0,2,3],[2,5,3]])

