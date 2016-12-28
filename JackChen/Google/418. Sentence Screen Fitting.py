

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
s.wordsTyping(["abc","de", 'f'], 4, 6)
