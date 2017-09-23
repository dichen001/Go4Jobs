"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2
Explanation:

Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # Think carefully, we can do it in O(N), because we
        # only care about the ending lenth for each brick, right?
        mem, ans = {}, len(wall)
        for row in wall:
            end = 0
            for brick in row[:-1]:
                end += brick
                mem[end] = mem.get(end, 0) + 1
        for end, passed in mem.iteritems():
            ans = min(ans, len(wall) - passed)
        return ans

        # O(N*log(H))
        wall = map(lambda w: collections.deque(w), wall)
        heapify(wall)
        ans = len(wall)
        while wall and len(wall[0]) > 1:
            cross, cut = 0, wall[0].popleft()
            wall[0][0] += cut
            for i in range(1, len(wall)):
                if wall[i][0] != cut:
                    cross += 1
                else:
                    wall[i].popleft()
                    wall[i][0] += cut
            ans = min(ans, cross)
            heapify(wall)
        return ans






