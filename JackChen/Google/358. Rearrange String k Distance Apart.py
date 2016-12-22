from heapq import *
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k <= 0:
            return str
        mem, n = {}, len(str)
        ans = ''
        for c in str:
            mem[c] = mem.get(c,0) + 1
        pairs = [(-cnt, c) for c, cnt in mem.iteritems()]
        heapify(pairs)
        next = {c:0 for c in mem.keys()}
        queue = []
        for i in range(n):
            cnt, c = heappop(pairs)
            ans += c
            if -cnt > 1:
                queue += [(-cnt+1, c)]
            if len(queue) < k:
                continue
            heappush(pairs, queue.pop(0))

        return ans




s = Solution()
s.rearrangeString("aaabc",2)
