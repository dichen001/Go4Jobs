import heapq
from collections import defaultdict
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # add all border points
        points, results = [], []
        mem = defaultdict(int)
        for b in buildings:
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort()
        q = [0]
        prev = 0
        for p in points:
            if p[1] < 0:
                heapq.heappush(q, p[1])
                mem[p[1]] += 1
            else:
                mem[p[1]] -= 1
            cur = heapq.heappop(q)
            while mem[cur] == 0:
                cur = heapq.heappop()
            heapq.heappush(q,cur)
            if prev != cur:
                results.append([p[0], -cur])
                prev = cur
        return results

s = Solution()
s.getSkyline([[0,2,3],[2,5,3]])

