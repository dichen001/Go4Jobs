from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        queue = [(v, 0, j) for j, v in enumerate(matrix[0])]
        heapify(queue)
        for i in range(k):
            t = heappop(queue)
            x, y = t[1], t[2]
            if x < m:
                heappush(queue, matrix[x+1][y])
        return t[0]


s = Solution()
s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
