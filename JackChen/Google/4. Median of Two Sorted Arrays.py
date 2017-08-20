"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return
        A, B = nums1, nums2
        l, r, half = 0, m, (m + n + 1) / 2
        while l <= r:
            i = (l + r) / 2
            j = half - i
            if i > 0 and A[i-1] > B[j]:
                r = i - 1
            # note it's very important here to have 'i < m' instead of 'j > 0' !!
            # because we are basically changing i here, j is just changed correspondingly with i.
            elif i < m and B[j-1] > A[i]:
                l = i + 1
            else:
                if i == 0:
                    max_l = B[j-1]
                elif j == 0:
                    max_l = A[i-1]
                else:
                    max_l = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return max_l
                if i == m:
                    min_r = B[j]
                elif j == n:
                    min_r = A[i]
                else:
                    min_r = min(A[i], B[j])
                return (max_l + min_r) / 2.0

s = Solution()
s.findMedianSortedArrays([1,3],[2])
