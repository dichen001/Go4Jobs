class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp (dp[i] = dp[i+1] + dp[i+2]) backward
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 0 if s[n - 1] == "0" else 1
        for i in range(n - 2, -1, -1):
            if s[i] != 0:
                dp[i] = dp[i + 1] + dp[i + 2] if int(s[i:i + 2]) < 27 else dp[i + 1]
        return dp[0]

        # # recursive (with memorization)
        # mem = {}
        # def getAll(s):
        #     if s in mem:
        #         return mem[s]
        #     if not s or len(s) == 1 and s[0] != "0":
        #         mem[s] = 1
        #     elif s[0] == "0":
        #         mem[s] = 0
        #         return 0
        #     elif int(s[:2]) > 26:
        #         mem[s] = getAll(s[1:])
        #     else:
        #         mem[s] = getAll(s[1:]) + getAll(s[2:])
        #     return mem[s]


        # # recursive TLE (without memorization)
        # def getAll(s):
        #     if not s or len(s) == 1 and s[0] != "0":
        #         return 1
        #     if s[0] == "0":
        #         return 0
        #     if int(s[:2]) > 26:
        #         return getAll(s[1:])
        #     return getAll(s[1:]) + getAll(s[2:])


        return getAll(s) if s else 0

s = Solution()
s.numDecodings("00")