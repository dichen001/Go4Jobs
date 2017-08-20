"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.


"""

import collections
from heapq import heappush, heappop, heapify

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        # O(NK) solution.
        window = sorted(nums[:k])
        ans = [window[(k + 1) / 2] if k % 2 else (window[k/2] + window[k/2 + 1]) / 2.0]
        for i, n in enumerate(nums[k:]):
            window.remove(nums[i])
            window.append(n)
            window.sort()
            ans += [window[(k + 1) / 2] if k % 2 else (window[k/2] + window[k/2 + 1]) / 2.0]
        return ans


        # init
        low, high = [], nums[:k]
        heapify(high)
        for _ in range( (k + 1) / 2 ):
            heappush(low, -heappop(high))
        ans = [-low[0]] if k % 2 else [(high[0] - low[0]) / 2.0]

        invalids = collections.defaultdict(int)

        for i, n in enumerate(nums[k:], k):
            balance = 0
            # process the out number
            out = nums[i-k]
            balance += -1 if out <= -low[0] else 1
            invalids[out] += 1

            # process the in number
            if not low or n <= -low[0]:
                heappush(low, -n)
                balance += 1
            else:
                heappush(high, n)
                balance -= 1

            # rebalance the valid number in low and high
            if balance < 0:
                heappush(low, -heappop(high))
            if balance > 0:
                heappush(high, -heappop(low))

            # remove the invalid numbers at the middle
            while low and invalids[-low[0]]:
                invalids[-heappop(low)] -= 1
            while high and invalids[high[0]]:
                invalids[heappop(high)] -= 1

            ans += [-low[0]] if k % 2 else [(high[0] - low[0]) / 2.0]
        return map(float, ans)



s = Solution()
s.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3)
