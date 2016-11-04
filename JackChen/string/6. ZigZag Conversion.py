"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        s = [c for c in s]
        r, n = [], len(s)
        for i in range(numRows):
            pos = i
            if pos < n:
                r.append(s[pos])
            go, steps = 0, [2*(numRows-1-i), 2*i]
            while pos < n:
                pos += steps[go]
                if pos >= n:
                    break
                if steps[go]:
                    r.append(s[pos])
                go = (go+1) % 2
        return ''.join(r)

