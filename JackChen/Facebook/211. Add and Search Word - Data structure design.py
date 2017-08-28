"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = collections.defaultdict(set)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.mem[len(word)].add(word)




    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if "." in word:
            for w in self.mem[len(word)]:
                for i, c in enumerate(word):
                    if w[i] != c and c != ".":
                        break
                    if i == len(word) - 1:
                        return True
        elif word != "":
            return word in self.mem[len(word)]
        return False






# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
