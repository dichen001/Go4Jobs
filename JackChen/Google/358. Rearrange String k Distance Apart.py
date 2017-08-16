import collections

from heapq import *
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        # """
        # mem = collections.Counter(s)
        # order = sorted([(n, c) for c, n in mem.iteritems()])
        # ans = ['*'] * len(s)
        # start = 0
        # while order:
        #     n, c = order.pop()
        #     n = max(n, len(order) + 1)
        #     for i in range(mem[c]):
        #         ans[start + n * i] = c
        #     start += 1
        # return ''.join(ans)
        order = sorted([(-n, c) for c, n in collections.Counter(s).iteritems()])
        heapify(order)
        ans, queue = "", []
        while len(ans) < len(s):
            if not order:   return ""
            n, c = heappop(order)
            ans += c
            if -n > 1:
                queue += [(n + 1, c)]
            if len(queue) < k:
                continue
            while queue:
                heappush(order, queue.pop())
        return ans



        if k <= 0:
            return str
        mem, n = {}, len(str)
        ans = ''
        for c in str:
            mem[c] = mem.get(c,0) + 1
        pairs = [(-cnt, c) for c, cnt in mem.iteritems()]
        heapify(pairs)
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
s.rearrangeString("abb",2)
