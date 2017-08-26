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
from heapq import heappush, heappop


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # O(Nlog(N))
        intervals.sort(key=lambda x: (x.start, x.end))
        ans = 0
        if intervals:
            ans, rooms = 1, [intervals[0].end]
        for interval in intervals[1:]:
            while rooms and interval.start >= rooms[0]:
                heappop(rooms)
            heappush(rooms, interval.end)
            ans = max(ans, len(rooms))
        return ans

        # worst case: O(N*2)
        intervals.sort(key=lambda x: (x.start, x.end))
        ans, rooms = 0, []
        for interval in intervals:
            s, e = interval.start, interval.end
            if not rooms:
                rooms.append(e)
            else:
                updated_rooms = []
                # it would be more efficient if the rooms are ordered by the end time
                # i.e. the top one has the smallest ending time, and will be the next free room.
                for i, room in enumerate(rooms):
                    if s < room:
                        updated_rooms.append(room)
                rooms = updated_rooms
                rooms.append(e)
            ans = max(ans, len(rooms))
        return ans

