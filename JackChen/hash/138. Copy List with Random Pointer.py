"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        mem = {}
        go = head
        while go:
            mem[go] = RandomListNode(go.label)
            go = go.next
        go = head
        while go:
            mem[go].next = mem.get(go.next, None)
            mem[go].random = mem.get(go.random, None)
            go = go.next
        return mem.get(head, None)

