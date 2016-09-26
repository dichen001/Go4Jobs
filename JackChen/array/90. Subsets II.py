"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = [[]]
        for n in nums:
            tmp_r = r[:]
            for exist in tmp_r:
                tmp = exist[:]
                #tmp.append(n)
                self.insertByOrder(tmp,n)
                if tmp not in r:
                    r.append(tmp)
        return r

    def insertByOrder(self, l, n):
        for i in range(len(l)):
            if n <= l[i]:
                l.insert(i,n)
                return l
        l.append(n)
        return l




s = Solution()
s.subsetsWithDup([1,2,2])
