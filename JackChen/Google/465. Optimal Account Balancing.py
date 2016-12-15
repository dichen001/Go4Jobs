import collections, sys
class Solution(object):
    def minTransfers(self, transactions):
        # Compute balance after all transactions for every person.
        balance = collections.defaultdict(int)
        for t in transactions:
            balance[t[0]] -= t[2]
            balance[t[1]] += t[2]
        # Preserve unsettled people only.
        final, cnt = [], 0
        for v in balance.values():
            if v != 0:
                final.append(v)
        # Remove the 1-Step transactions that settles 2 =
        for v in final:
            if -v in final:
                while v in final and -v in final:
                    final.remove(v)
                    final.remove(-v)
                    cnt += 1
        return self.traverse(final, 0, cnt)

    def traverse(self, net, start, count):
        # Skip settled people.
        while start < len(net) and net[start] == 0:
            start += 1
        if start + 1 >= len(net):
            return count
        minimum = sys.maxint
        for i in range(start + 1, len(net)):
            # try all possible closing out in the future.
            if net[start] * net[i] < 0:
                net[i] += net[start]
                minimum = min(minimum, self.traverse(net, start + 1, count + 1))
                net[i] -= net[start]
        return minimum

s = Solution()
s.minTransfers([[0,3,2],[1,4,3],[2,3,2],[2,4,2]])
