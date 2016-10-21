"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        r = []
        nums = [str(i) for i in range(1, n+1)]
        nn = 1
        bin_length = [1]
        # [1,1,2,6,24]
        for i in range(1, n):
            nn *= i
            bin_length.append(nn)
        for i in range(1, n+1):
            index = (k-1) / bin_length[n-i]
            r.append(nums[index])
            nums.remove(nums[index])
            k -= index * bin_length[n-i]
        return ''.join(r)
