"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i, n, L = 0, len(words), maxWidth
        ans, cur, curL = [], [], 0
        for w in words:
            if curL + len(cur) + len(w) > L:
                insertion = (len(cur) -1 ) or 1
                for i in range(L - curL):
                    cur[i % insertion] += ' '
                ans.append(''.join(cur))
                cur, curL = [], 0
            cur += [w]
            curL += len(w)
        return ans + [" ".join(cur) + (L-curL-len(cur)+1) * ' ']


