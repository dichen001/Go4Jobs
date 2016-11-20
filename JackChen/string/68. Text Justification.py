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
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # Their Solusion is so concise
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]



        # My Own Implementation is so ugly...
        def formnewline(line, last):
            if last:
                newline = " ".join(line)
                rest = maxWidth - len(newline)
                newline += " " * rest
            else:
                l = maxWidth - len(''.join(line))
                if l == 0:
                    return ' '.join(line)
                n = len(line) - 1
                if n <= 0:
                    return line[0] + ' ' * l
                big_num = l % n
                big_width = l/n + 1
                small_num = n - big_num
                small_width = l/n
                widths = [" " * big_width] * big_num + [" " * small_width] * small_num
                newline = line[0]
                for i, s in enumerate(widths, 1):
                    newline += s + line[i]
            return newline

        cnt, newline, result = 0, [], []
        appended = False
        for i, w in enumerate(words):
            if len(w) + cnt <= maxWidth:
                newline.append(w)
                cnt += len(w) + 1
                appended = False
            else:
                result.append(formnewline(newline, i == len(words)-1 and (words[i] in newline or words[i] == '')))
                newline = [w]
                cnt = len(w) + 1
                appended = True
        if newline:
            result.append(formnewline(newline, True))
        return result

s = Solution()
print s.fullJustify(["Here","is","an","example","of","text","justification."], 16)
