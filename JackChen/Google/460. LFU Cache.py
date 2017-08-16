"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

PRE, NEXT, KEY, VAL, FREQ = 0, 1, 2, 3, 4


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_map = {}
        self.freq_map = {}
        self.cap = capacity
        self.min_freq = 1

    def removeNode(self, node):
        node[PRE][NEXT], node[NEXT][PRE] = node[NEXT], node[PRE]

    def addNode(self, node, freq):
        key_map, freq_map = self.key_map, self.freq_map
        freq_head = freq_map.setdefault(freq, [])
        if not freq_head:
            freq_head[:] = [freq_head, freq_head, None, None, freq]
        # update and add the node to the end of the freq node list
        node[FREQ] = freq
        node[PRE], node[NEXT] = freq_head[PRE], freq_head
        freq_head[PRE][NEXT], freq_head[PRE] = node, node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        key_map, freq_map = self.key_map, self.freq_map
        if key not in key_map:
            return -1
        node = key_map[key]
        self.removeNode(node)
        # update the min freq if only 1 freq node exist
        if freq_map[self.min_freq] is freq_map[self.min_freq][NEXT]:
            self.min_freq += 1
        self.addNode(node, node[FREQ] + 1)
        return key_map[key][VAL]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        key_map, freq_map = self.key_map, self.freq_map
        if self.cap < 1:
            return
        if key in key_map:
            key_map[key][VAL] = value
            self.get(key)
        else:
            # check and remove the 1st node in the minimum freq node list.
            if len(key_map) == self.cap:
                node2evict = freq_map[self.min_freq][NEXT]
                self.removeNode(node2evict)
                del key_map[node2evict[KEY]]
            self.min_freq = 1
            node = [None, None, key, value, 1]
            self.addNode(node, node[FREQ])
            key_map[key] = node



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