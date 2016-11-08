"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        results = []
        for i in sorted(intervals, key=lambda x: x.start):
            if results and i.start <= results[-1].end:
                results[-1].end = max(results[-1].end, i.end)
            else:
                results += [i]
        return results

        ## my 1st try... too redundent
        results = []
        if not intervals:
            return results
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        for i in intervals[1:]:
            if i.start in range(start, end + 1):
                end = max(end, i.end)
            else:
                interval = Interval(s=start, e=end)
                results.append(interval)
                start, end = i.start, i.end
        interval = Interval(s=start, e=end)
        results.append(interval)
        return results

