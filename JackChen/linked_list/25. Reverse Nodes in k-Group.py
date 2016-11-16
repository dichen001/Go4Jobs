"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        rhead, n, stack = None, 0, []
        node = head
        pre_head = ListNode(-1)
        pre_head.next = head
        while node and n == 0:
            while node and n < k:
                stack.append(node)
                node = node.next
                n += 1
            if k > 0 and len(stack) == k:
                n = 0
                head = stack.pop()
                node = head
                next = node.next
                if not rhead:
                    rhead = head
                while stack:
                    pre = stack.pop()
                    node.next = pre
                    node = pre
                node.next = next
                pre_head.next = head
                pre_head = node
                node = next
        return rhead if rhead else head


s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
r = s.reverseKGroup(ListNode(1), 2)
