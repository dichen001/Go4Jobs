"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # O(Nlog(K))
        import heapq
        q, uglyNums = [], [1]
        k = len(primes)
        for i in range(k): heapq.heappush(q, (primes[i], 0, primes[i]))
        while len(uglyNums) < n:
            x, i, p = q[0]
            uglyNums += [x]
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * uglyNums[i+1], i+1, p))
        return uglyNums[-1]


        # O(KN)
        k = len(primes)
        prime_counter = [0] * k
        ugly = [0] * n
        ugly[0] = 1
        values = [1] * k
        for i in range(1, n):
            ugly[i] = float("inf")
            for j in range(k):
                if values[j] == ugly[i-1]:
                    values[j] = primes[j] * ugly[prime_counter[j]]
                    prime_counter[j] += 1
                ugly[i] = min(ugly[i], values[j])

            # for j in range(k):
            #     ugly[i] = min(ugly[i], primes[j] * ugly[prime_counter[j]])
            # for j in range(k):
            #     while primes[j] * ugly[prime_counter[j]] == ugly[i]:
            #         prime_counter[j] += 1

        return ugly[n-1]
