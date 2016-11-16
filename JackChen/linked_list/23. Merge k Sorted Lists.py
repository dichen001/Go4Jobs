# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        head = ListNode(-1)
        cur = head
        for l in lists:
            if l: heapq.heappush(q, (l.val, l))
        while q:
            cur.next = heapq.heappop(q)[1]
            cur = cur.next
            if cur.next: heapq.heappush(q, (cur.next.val, cur.next))
        return head.next
