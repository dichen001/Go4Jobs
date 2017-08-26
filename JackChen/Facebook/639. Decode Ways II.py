"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        #*, 1*, 2*
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == "*":
                # treat c as single
                f0 = 9*e0 + 9*e1 + 6*e2
                # treat c as 1, then it's fixed and next e1,
                # which is f1, is eaqual to e0
                f1 = e0
                # treat c as 2, then it's fixed and next e2,
                # which is f2, is eaqual to e0
                f2 = e0
            else:
                f0 = (c != "0") * e0 + e1 + (c <= "6") * e2
                # next e1, which is f1, is implying c == 1
                f1 = (c == "1") * e0
                # next e2, which is f2, is implying c == 2
                f2 = (c == "2") * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0