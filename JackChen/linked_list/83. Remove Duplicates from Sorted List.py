"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rhead = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return rhead

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)

h = ListNode(2)
h.next = ListNode(3)

r = s.swapPairs(h)
