"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # optimazed. Bi-BFS
        front, back = {beginWord}, {endWord}
        wordList = set(wordList)
        if endWord not in wordList: return 0
        dist, word_len = 1, len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.lowercase:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in back:
                            return dist
                        if new_word in wordList:
                            next_front.add(new_word)
                            wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0

        # first try. BFS
        steps, Q = 0, collections.deque([beginWord])
        atoz = map(chr, range(ord("a"), ord("z")))
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        step = 1
        visited = set()
        while Q:
            count = len(Q)
            step += 1
            for _ in range(count):
                w = Q.popleft()
                for i in range(len(w)):
                    for c in atoz:
                        nw = w[:i] + c + w[i + 1:]
                        if nw == endWord:
                            return step
                        if nw not in visited and nw in wordList:
                            visited.add(nw)
                            Q.append(nw)

        return 0


