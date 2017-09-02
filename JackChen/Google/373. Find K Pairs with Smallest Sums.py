"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""

from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # O(Klog(K))  Only need to maintain a Q of length K.
        ans = []
        if not nums1 or not nums2:
            return ans
        Q = [(n + nums2[0], n, nums2[0], 0) for n in nums1[:k]]
        heapify(Q)
        for _ in range(k):
            if not Q:
                return ans
            n12, n1, n2, i2 = heappop(Q)
            ans.append([n1, n2])
            if i2 == len(nums2) - 1:
                continue
            heappush(Q, (n1 + nums2[i2 + 1], n1, nums2[i2 + 1], i2+1))
        return ans

        # brute force
        queue = [(m+n, m ,n) for m in nums1 for n in nums2]
        heapify(queue)
        ans = []
        while queue and len(ans) < k:
            ans += [heappop(queue)[1:]]
        return ans
        
        
        
