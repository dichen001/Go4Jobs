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
        # Merge Sort Count
        def MSC(enums):
            mid = len(enums) /2
            if mid:
                left, right = MSC(enums[:mid]), MSC(enums[mid:])
                for i in range(len(enums))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        result[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
            return enums

        result = [0] * len(nums)
        MSC(list(enumerate(nums)))
        return result

s = Solution()
s.countSmaller([5, 2, 6, 1])
