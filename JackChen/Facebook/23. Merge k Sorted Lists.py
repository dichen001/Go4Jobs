"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        cur, heap = head, []
        for node in lists:
            if node:
                heappush(heap, (node.val, node))
        while heap:
            cur.next = heappop(heap)[1]
            cur = cur.next
            if cur.next:
                heappush(heap, (cur.next.val, cur.next))
        return head.next

