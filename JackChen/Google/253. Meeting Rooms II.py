"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key= lambda x: (x.start, x.end))
        ans, rooms = 0, []
        if intervals:
            rooms.append(intervals[0].end)
            ans = 1
        for interval in intervals[1:]:
            while rooms and interval.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
            ans = max(ans, len(rooms))
        return ans
