import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # envelopes = map(lambda x: [x[0], -x[1]], envelopes)
        # envelopes.sort()
        # heights = [-x[1] for x in envelopes]
        # dp, max_size = [0] * len(heights), 0
        # for h in heights:
        #     left, right = 0, max_size
        #     size = bisect.bisect_left(dp, h, left, right)
        #     dp[size] = h
        #     max_size = max(max_size, size + 1)
        # return max_size
        envelopes.sort(key=(lambda x: (x[0], -x[1])))
        heights = [-x[1] for x in envelopes]
        asceding, ans = [0] * len(heights), 0
        for h in heights:
            l, r = 0, ans
            size = bisect.bisect_left(asceding, h, l, r)
            asceding[size] = h
            ans = max(ans, size + 1)
        return ans

s = Solution()
# s.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])
s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])