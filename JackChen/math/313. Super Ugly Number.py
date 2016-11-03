class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if primes and primes[0] != 1:
            primes.insert(0, 1)
        U, k = [1], len(primes)
        pid = [0] * k
        while len(U) < n :
            candidates = [U[pid[i]] * primes[i] for i in range(1, k)]
            next = min(candidates)
            U.append(next)
            for i in range(1, k):
                while U[pid[i]] * primes[i] <= next:
                    pid[i] += 1
        return U[n-1]

s = Solution()
s.nthSuperUglyNumber(35, [2,3,11,13,17,23,29,31,37,47])
