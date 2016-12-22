"""
Given a non-negative number represented as a singly linked list of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
Show Company Tags
Show Tags
Show Similar Problems
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        flag = False
        while head and head.next:
            stack.append(head)
            head = head.next
        head.val += 1
        if head.val > 9:
            head.val = 0
            flag = True
        while stack:
            head = stack.pop()
            if flag:
                head.val += 1
                if head.val > 9:
                    flag = True
                    head.val = 0
                else:
                    flag = False
        if flag:
            new_head = ListNode(1)
            new_head.next = head
            head = new_head
        return head

