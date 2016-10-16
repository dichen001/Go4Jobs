"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        result, add = head, 0
        while l1 or l2:
            tmp = l1.val if l1 else 0
            tmp += l2.val if l2 else 0
            tmp += add
            add = 0 if tmp < 10 else 1
            tmp = tmp-10 if add else tmp
            head.next = ListNode(tmp)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if add:
            head.next = ListNode(1)
        return result.next

