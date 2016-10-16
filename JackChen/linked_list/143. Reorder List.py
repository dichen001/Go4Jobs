"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        rev, rev_head = None, p1.next
        while rev_head:
            rev, rev.next, rev_head = rev_head, rev, rev_head.next
        p1.next = None
        while head and rev:
            head.next, rev.next, head, rev = rev, head.next, head.next, rev.next
