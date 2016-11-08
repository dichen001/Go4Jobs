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
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        if n1 == 0:
            return (nums2[(n2-1)/2] + nums2[(n2)/2]) / float(2)
        low, high = 0, 2*n1
        while low <= high:
            m1 = (low + high) /2
            m2 = n1 + n2 - m1
            l1 = nums1[(m1-1)/2] if m1 !=0 else float('-inf')
            l2 = nums2[(m2-1)/2] if m2 !=0 else float('-inf')
            r1 = nums1[m1/2] if m1 != 2*n1 else float('inf')
            r2 = nums2[m2/2] if m2 != 2*n2 else float('inf')
            if l1 >= r2:
                high = m1 - 1
            elif l2 >= r1:
                low = m1 + 1
            else:
                return (max(l1, l2) + min(r1, r2)) / float(2)
        return (max(l1, l2) + min(r1, r2)) / float(2)
