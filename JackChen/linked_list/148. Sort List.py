"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(h1, h2):
            pre = ListNode(0)
            go = pre
            while h1 and h2:
                if h1.val < h2.val:
                    go.next = h1
                    h1 = h1.next
                else:
                    go.next = h2
                    h2 = h2.next
                go = go.next
            if h1:
                go.next = h1
            if h2:
                go.next = h2
            return pre.next

        if not head or not head.next:
            return head
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        h1, h2 = head, slow.next
        slow.next = None
        return merge(self.sortList(h1), self.sortList(h2))


