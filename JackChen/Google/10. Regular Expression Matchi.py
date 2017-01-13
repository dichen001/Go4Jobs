class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s or not p:
            return False
        ls, lp = len(s), len(p)
        mem = [[False] * (lp+1) for _ in range(ls+1)]
        mem[0][0] = True
        # process '*' matches for all empty string first.  e.g. 'a*' ---> '': True
        for j in range(2, lp+1):
            if p[j-1] == '*' and mem[0][j-2]:
                mem[0][j] = True
        # precess others
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    mem[i][j] = mem[i-1][j-1]
                if p[j-1] == '*':
                    if p[j-2] != s[i-1] or p[j-2] != '.':
                        mem[i][j] = mem[i][j-2]
                    else:
                        mem[i][j] = mem[i][j-2] or mem[i][j-1] or mem[i-1][j]
        return mem[ls][lp]

s = Solution()
s.isMatch('aa', 'a*')