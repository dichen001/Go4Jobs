class Union(object):
    def __init__(self, n):
        self.root, self.size = range(n), [1] * n

    def find(self, n):
        root = self.root
        while root[n] != n:
            root[n] = root[root[n]]
            n = root[n]
        return n

    def union(self, a, b):
        root, size = self.root, self.size
        a, b = self.find(a), self.find(b)
        if size[a] < size[b]:
            root[a] = root[b]
            size[b] += size[a]
        else:
            root[b] = root[a]
            size[a] += size[b]


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        union = Union(len(nums))
        mem = {}
        for i, n in enumerate(nums):
            mem[n] = i
            if n - 1 in mem:
                union.union(mem[n], mem[n - 1])
            if n + 1 in mem:
                union.union(mem[n], mem[n + 1])
        return max(union.size)


s =Solution()
s.longestConsecutive([100,4,200,1,3,2])