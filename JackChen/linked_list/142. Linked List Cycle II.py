"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
