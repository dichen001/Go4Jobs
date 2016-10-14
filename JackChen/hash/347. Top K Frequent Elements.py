"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## bucket sorts  O(n)
        hash, result = {}, []
        for n in nums:
            hash[n] = hash.get(n, 0) + 1
        counts = [[] for i in range(len(nums) + 1)]
        for num, count in hash.iteritems():
            counts[count].append(num)
        for i in range(len(nums), 0, -1):
            if len(result) < k and counts[i] != []:
                result.extend(counts[i])
        return result

        ## O(nlog(n))
        max.sort(reverse=True)
        for key in hash.keys():
            if hash[key] in max[0:k]:
                result.append(key)
        result.sort()
        return result
