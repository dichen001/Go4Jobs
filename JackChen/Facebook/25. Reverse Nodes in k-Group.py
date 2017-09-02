"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Iterative
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while True:
            rev, cnt = head, 0
            while rev and cnt < k:
                rev = rev.next
                cnt += 1
            if cnt < k:
                return dummy.next
            nextPre = head
            for _ in range(k):
                head.next, rev, head = rev, head, head.next
            pre.next = rev
            pre = nextPre
        return dummy.next


        # Recursive
        rev, cnt = head, 0
        while rev and cnt < k:
            rev = rev.next
            cnt += 1
        if cnt == k:
            rev = self.reverseKGroup(rev, k)
            for _ in range(k):
                head.next, rev, head = rev, head, head.next
            head = rev
        return head



n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

s = Solution()
s.reverseKGroup(n1, 3)
