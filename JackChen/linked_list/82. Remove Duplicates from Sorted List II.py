"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        flag, result, pre.next = False, pre, head
        while head:
            if head.next and head.val == head.next.val:
                flag, head.next = True, head.next.next
            elif flag:
                flag, pre.next, head= False, head.next, head.next
            else:
                pre, head = pre.next, head.next
        return result.next
