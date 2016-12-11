"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  # (pre, pre_size)
        i, n = 0, len(s)
        cur, result = '', ''
        while i < n:
            if s[i].isdigit():
                num = []
                while s[i].isdigit():
                    num.append(s[i])
                    i += 1
                num = ''.join(num)
                stack.append([cur, int(num)])
                cur = ''
            elif s[i].isalpha():
                cur += s[i]
            else:
                # ']'
                tmp = stack[-1][0] + stack[-1][1] * cur
                cur = tmp
                stack.pop()
                if not stack:
                    result += cur
                    cur = ''
            i += 1
        return result + cur
