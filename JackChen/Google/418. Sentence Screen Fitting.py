"""
Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        l = len(s)
        adjustment = [0] * l
        for i, c in enumerate(s[1:], 1):
            adjustment[i] = 1 if c == ' ' else adjustment[i-1] - 1
        valid = 0
        for r in range(rows):
            valid += cols
            valid += adjustment[valid % l]
        return valid / l


        "wrong and TLE"
        mem = [0] * rows
        width = [len(w) for w in sentence]
        cnt, n = 0, len(sentence)
        i, col, row = 0, 0, 0
        while row < rows:
            if col + width[i] <= cols:
                col += width[i] + 1
                i += 1
                if i == n:
                    i = 0
                    col_repeat = (cols - col) / col if cols > col else 0
                    cnt += 1 + col_repeat
                    col += col * col_repeat
                    mem[row] = cnt
                    if col + width[i] > cols:
                        repeat = (rows - row - 1) / (row+1)
                        left = (rows - row - 1) % (row+1)
                        return cnt * (repeat+1) + mem[left-1] if row < rows - 1 else cnt
            if row > 0 and mem[row] < mem[row-1]:
                mem[row] = mem[row-1]
            if col + width[i] > cols:
                col = 0
                row += 1
        return cnt






s = Solution()
# s.wordsTyping(["a"], 2, 3)
# s.wordsTyping(["a","bcd", "e"], 5, 6)
s.wordsTyping(["a","bcd"], 20000, 20000)
