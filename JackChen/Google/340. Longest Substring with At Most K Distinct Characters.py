"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        "much faster solution"
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            ## O(klog(k)) cause the maximum size of d is k ##
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret

        "2nd "
        l, n = 0, len(s)
        mem = {}
        max_len = 0
        distinct = 0
        for r in range(n):
            if not mem.get(s[r]):
                distinct += 1
            mem[s[r]] = mem.get(s[r]) + 1 if mem.get(s[r]) else 1
            while distinct > k:
                mem[s[l]] -= 1
                if mem[s[l]] == 0:
                    distinct -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len


        # 1st stupid DP solusion, O(n^2)
        if k < 1:
            return 0
        n = len(s)
        dp = [[[[], 0] for i in range(n+1)] for _ in range(n)]
        max_len = [0]

        def getMax(dp,l,r,c):
            if dp[l][r][0] or l >= r:
                return dp[l][r][0], dp[l][r][1]
            else:
                if c in dp[l][r-1][0]:
                    dp[l][r][0] = dp[l][r-1][0] + [c]
                    dp[l][r][1] = dp[l][r-1][1] if dp[l][r-1][1] > 0 else 1
                elif dp[l][r-1][1] < k:
                    dp[l][r][0] = dp[l][r-1][0] + [c]
                    dp[l][r][1] = dp[l][r-1][1] + 1
                else:
                    dp[l][r][0], dp[l][r][1] = getMax(dp, l+1, r, c)
                if len(dp[l][r][0]) > max_len[0]:
                    max_len[0] = len(dp[l][r][0])
                return dp[l][r][0], dp[l][r][1]

        for i in range(n-1,-1,-1):
            for j in range(i+1, n+1):
                c = s[j-1]
                getMax(dp, i,j, c)

        return max_len[0]

        # dp[n] = dp[n-1][0] if dp[n-1]
