import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS Fast!
        squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        queue = [n]
        level = 0
        while queue:
            level += 1
            size = len(queue)
            for i in range(size):
                remaining = queue.pop(0)
                for square in squares:
                    if square == remaining:
                        return level
                    if square > remaining:
                        break
                    queue.append(remaining-square)
        return level



        # DFS Slow!!!
        def dfs(n):
            if n == 0 or mem[n] != float('inf'):
                return mem[n]
            for i in squres:
                if i > n:
                    break
                mem[n] = min(mem[n], 1 + dfs(n-i))

        squres = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        mem = [0] + [float('inf')] * n
        for i in range(1, n+1):
            dfs(i)
        return mem[n]

s = Solution()
s.numSquares(7168)