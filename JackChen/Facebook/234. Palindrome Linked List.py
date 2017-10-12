"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # rev, fast = None, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     rev, rev.next, head = head, rev, head.next
        # slow = head.next if fast else head
        # ans = True
        # while rev:
        #     ans = ans and rev.val == slow.val
        #     head, head.next, rev = rev, head, rev.next
        #     slow = slow.next
        # return ans
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = rev
            rev = slow
            slow = tmp
        right = slow.next if fast else slow
        ans = True
        while rev:
            ans = ans and rev.val == right.val
            right = right.next
            tmp = rev.next
            rev.next = slow
            slow = rev
            rev = tmp
        return ans


n = ListNode(0)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(3)
s = Solution()
s.isPalindrome(n)
