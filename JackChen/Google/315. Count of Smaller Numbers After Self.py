"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def mergesort(enums):
            m = len(enums) / 2
            if m:
                left, right = mergesort(enums[:m]), mergesort(enums[m:])
                for i in range(len(enums))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        answer[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
            return enums

        answer = [0] * len(nums)
        mergesort(list(enumerate(nums)))
        return answer


for i, x, y in enumerate([(1,2), (3,4)]):
    print x
    print y