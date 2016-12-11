"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Show Company Tags
Show Tags
Show Similar Problems

"""

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words or not words[0]:
            return []
        squares, prefix = [], collections.defaultdict(list)
        l = len(words[0])
        for w in words:
            for i in range(1,l+1):
                prefix[w[:i]] += [w]
        def build(square):
            if len(square) == l:
                squares.append(square)
                return
            for w in prefix[''.join(zip(*square)[len(square)])]:
                build(square + [w])
        for w in words:
            build([w])
        return squares



