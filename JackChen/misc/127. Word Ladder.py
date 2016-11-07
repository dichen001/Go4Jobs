"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # BFS
        front, back=set([beginWord]), set([endWord])
        depth, width = 2, len(beginWord)
        charSet = list(string.lowercase)
        wordDict = wordList - set([beginWord, endWord])
        while front:
            newFront = set()
            for phrase in front:
                for i in xrange(width):
                    for c in charSet:
                        nw = phrase[:i]+c+phrase[i+1:]
                        if nw in back:
                            return depth
                        if nw in wordDict:
                            newFront.add(nw)
            front = newFront
            if len(front)>len(back):
                front, back = back, front
            wordDict -= front
            depth += 1
        return 0


s = Solution()
s.ladderLength('ta', 'if', ["ts","sc","ph","ca","jr","hf","to","if","ha","is","io","cf","ta"])
