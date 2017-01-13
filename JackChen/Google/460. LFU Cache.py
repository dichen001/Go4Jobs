class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        head, tail = Node(), Node()
        head.next = tail
        tail.pre = head

        self.head = head
        self.tail = tail
        self.hash = {}
        self.count = 0
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            value = node.val
            self.remove(node)
            self.insert(node)
            return value
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.hash[key] = node
            self.count += 1
            if self.count > self.capacity:
                self.count -= 1
                last = self.tail.pre
                del self.hash[last.key]
                self.remove(last)


    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


    def insert(self, node):
        node.next = self.head.next
        node.pre = self.head
        node.next.pre = node
        self.head.next = node






# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(3)
print obj.put(2,2)
print obj.put(1,1)
print obj.get(2)
print obj.get(1)
print obj.get(2)
print obj.put(3,3)
print obj.put(4,4)
print obj.get(3)
print obj.get(2)
print obj.get(1)
print obj.get(4)