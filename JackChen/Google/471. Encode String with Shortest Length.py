"""
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:
k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
"""

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n = len(s)
        mem = [[''] * n for _ in xrange(n)]
        # note that recurse from left, right and middle is not working!
        # Because the logic is inside out, not left to right
        # for i in range(n-1, 0, -1):
        #     for j in range(i, n):
        for l in range(n):
            for i in range(0, n-l):
                j = i + l
                mem[i][j] = s[i:j+1]
                if l + 1 <= 4:
                # if j - i + 1 <= 4:
                    continue
                for k in range(i, j):
                    left = mem[i][k]
                    right = mem[k+1][j]
                    if len(left) + len(right) < len(mem[i][j]):
                        mem[i][j] = left + right
                pos = (s[i:j+1] * 2)[1:-1].find(s[i:j+1])
                if pos > -1:
                    cnt = len(s[i:j+1]) / (pos+1)
                    ## It's very important to use mem[i][i+pos] here, instead of s[i:j+1][:pos+1]
                    abbr = str(cnt) + '[' + mem[i][i+pos] + ']'
                    if len(abbr) < mem[i][j]:
                        mem[i][j] = abbr
        return mem[0][n-1]

s = Solution()
s.encode("abbbabbbcabbbabbbc")