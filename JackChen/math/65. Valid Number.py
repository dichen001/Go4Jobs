"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def removeS(s):
            if s and s[0] in ('+', '-'):
                return s[1:]
            return s

        s = s.strip()
        if not s or ' ' in s:
            return False
        s = s.split('e')
        if s and len(s) == 1:
            s = s[0].split('.')
            s[0] = removeS(s[0])
            if len(s) == 1:
                return s[0] != '' and s[0].isdigit()
            if len(s) == 2:
                return (s[0].isdigit() and s[1].isdigit()) or (not s[0] and s[1].isdigit()) or (not s[1] and s[0].isdigit())
        if len(s) == 2:
            s[1] = removeS(s[1])
            if s[1] and s[1].isdigit():
                return self.isNumber(s[0])
        return False
