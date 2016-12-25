"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.word = ''


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = TrieNode()
            node = node.dict[c]
        node.word = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if node.dict and node.dict.get(c):
                node = node.dict[c]
            else:
                return False
        return node.word == word



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i, c in enumerate(prefix):
            if node.dict and node.dict.get(c):
               node = node.dict[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
