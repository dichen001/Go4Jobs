"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # while it easier if we sort it by h
        people.sort(key=lambda (h,k):(-h,k))
        queue = []
        for p in people:
            queue.insert(p[1],p)
        return queue

        # my 1st solution, sorted by and thought by k.
        people.sort(key= lambda s: (s[1],s[0]))
        queue = []
        for p in people:
            h, k = p[0], p[1]
            if k == 0:
                queue.append(p)
            else:
                size = len(queue)
                higher = 0
                inserted = False
                for i in range(size):
                    if queue[i][0] >= h:
                        higher += 1
                    if higher > k:
                        queue.insert(i, p)
                        inserted = True
                        break
                if not inserted:
                    queue.append(p)
        return queue


