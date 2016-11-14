"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from fractions import gcd
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        for i, fix_p in enumerate(points):
            mem, local_max, p_at_fix_p = {}, 0, 1
            for j, rest_p in enumerate(points[i+1:]):
                x, y = fix_p.x - rest_p.x, fix_p.y - rest_p.y
                if x == 0 and y == 0:
                    p_at_fix_p += 1
                    continue
                GCD = gcd(x, y)
                if GCD:
                    x, y = x/GCD, y/GCD
                key = ','.join([str(x), str(y)])
                mem[key] = mem.get(key, 0) + 1
                local_max = max(local_max, mem[key])
            result = max(result, local_max + p_at_fix_p)
        return result
