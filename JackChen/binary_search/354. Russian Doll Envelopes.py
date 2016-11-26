import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = map(lambda x: [x[0],-x[1]], envelopes)
        envelopes.sort()
        heights = [ -x[1] for x in envelopes]
        dp, max_size = [0]*len(heights), 0
        for h in heights:
            left, right = 0, max_size
            "could use package"
            # size = bisect.bisect_left(dp, h, left, right)

            "also could implement by yourself"
            while left < right:
                mid = (left + right) / 2
                if h > dp[mid]:
                    left = mid + 1
                else:
                    right = mid
            size = left

            dp[size] = h
            max_size = max(max_size, size + 1)
        return max_size

