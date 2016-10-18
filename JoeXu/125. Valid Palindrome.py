class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = []
        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z': 
                newS.append(i)
            elif 'A' <= i <= 'Z': 
                newS.append(chr(ord(i) - ord('A') + ord('a')))
        return newS == newS[::-1]