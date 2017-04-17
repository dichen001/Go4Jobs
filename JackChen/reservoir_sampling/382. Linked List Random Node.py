# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.h = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.h
        reservoir = node.val
        cnt = 0
        while node.next:
            cnt += 1
            node = node.next
            if cnt == random.randint(0, cnt):
                reservoir = node.val
        return reservoir


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()