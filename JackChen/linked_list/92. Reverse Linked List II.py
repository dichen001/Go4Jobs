"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        pre, dummy.next = dummy, head
        for _ in xrange(m-1):
            pre = pre.next
        start = pre.next
        then = pre.next.next
        for _ in xrange(n-m):
            start.next, then.next, pre.next = then.next, pre.next, then
            then = start.next
        return dummy.next

s = Solution()
h = ListNode(3)
h.next = ListNode(5)
h.next.next = ListNode(7)
r = s.reverseBetween(h,1,3)


