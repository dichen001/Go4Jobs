"""
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
Show Company Tags
Show Tags
Show Similar Problems

"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = [_ for _ in (v1,v2) if _]


        # self.v12 = [v1,v2]
        # self.i = 0
        # self.turn = 0


    def next(self):
        """
        :rtype: int
        """
        v = self.q.pop(0)
        ret = v.pop(0)
        if v:
            self.q.append(v)
        return ret

        # t = self.turn
        # i = self.i
        # v = self.v12[t][i]
        # self.turn = (t+1) % 2
        # if self.turn == 0 or self.i >= len(self.v12[(t+1) % 2]):
        #     self.i += 1
        # return v




    def hasNext(self):
        """
        :rtype: bool
        """
        if self.q:
            return True
        return False
        # t = self.turn
        # if self.i < len(self.v12[t]):
        #     return True
        # elif self.i < len(self.v12[(t+1)%2]):
        #     self.turn = (t+1) % 2
        #     return True
        # return False


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
