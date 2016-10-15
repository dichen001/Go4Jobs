"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow = slow.next
        return head


s = Solution()
h = ListNode(1)
# h.next = ListNode(2)
# h.next.next = ListNode(3)
# h.next.next.next = ListNode(4)
r = s.removeNthFromEnd(h,1)
