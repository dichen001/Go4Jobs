"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
"""

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        points = set() #collections.defaultdict(int)
        x1, x2, y1, y2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        area = 0
        for r in rectangles:
            x1 = min(x1, r[0])
            y1 = min(y1, r[1])
            x2 = max(x2, r[2])
            y2 = max(y2, r[3])
            area += (r[2] - r[0]) * (r[3] - r[1])
            for p in [(r[0],r[1]), (r[0],r[3]), (r[2],r[1]),  (r[2],r[3])]:
                if p not in points:
                    points.add(p)
                else:
                    points.remove(p)
        expected_points  = {(x1,y1), (x1,y2), (x2,y1), (x2,y2)}
        expected_area = (x2-x1) * (y2-y1)
        return area == expected_area and  points == expected_points
