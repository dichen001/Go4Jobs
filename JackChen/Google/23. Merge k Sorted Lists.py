"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heapify, heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or not lists[0]: return []
        mem = {(head.val, i): head for i, head in enumerate(lists) if head}
        # mem = {}
        # for i, head in enumerate(lists):
        #     if head:
        #         mem[(head.val, i)] = head
        Q = mem.keys()
        heapify(Q)
        ans = ListNode('start')
        node = ans
        while Q:
            val, i = heappop(Q)
            node.next = ListNode(val)
            node = node.next
            head = mem[(val, i)]
            del mem[(val, i)]
            if head.next:
                head = head.next
                mem[(head.val, i)] = head
                heappush(Q, (head.val, i))
        return ans.next

s = Solution()
s.mergeKLists([None,ListNode(-1)])