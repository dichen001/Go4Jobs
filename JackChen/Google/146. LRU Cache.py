"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
       javascript:void(0); :type capacity: int
        """
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.head.pre = None
        self.tail.pre = self.head
        self.tail.next = None
        self.count = 0
        self.capacity = capacity
        self.hash = {}

    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add2head(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node


    def get(self, key):
        """
        :rtype: int
        """
        if self.hash.get(key, 0):
            node = self.hash[key]
            self.deleteNode(node)
            self.add2head(node)
            return node.val
        return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.hash.get(key, 0):
            node = self.hash[key]
            node.val = value
            self.deleteNode(node)
            self.add2head(node)
        else:
            self.count += 1
            node = Node(key,value)
            self.hash[key] = node
            self.add2head(node)
            if self.count > self.capacity:
                del self.hash[self.tail.pre.key]
                self.deleteNode(self.tail.pre)