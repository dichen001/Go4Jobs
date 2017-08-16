"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]
        intervals.sort()
        s, e = newInterval.start, newInterval.end
        ans = []
        while intervals:
            l, r = intervals[0].start, intervals[0].end
            intervals.pop(0)
            if l <= s <= r or l <= e <= r or s <= l <= e or s <= r <= e:
                l = min(l, s)
                while intervals and e >= intervals[0].start:
                    r = intervals.pop(0).end
                r = max(r, e)
            ans += [Interval(l, r)]
        if s > ans[-1].end:
            ans += [Interval(s, e)]
        elif e < ans[0].start:
            ans = [Interval(s, e)] + ans
        return ans


s = Solution()
s.insert([Interval(1, 5), Interval(6, 8)], Interval(5, 6))