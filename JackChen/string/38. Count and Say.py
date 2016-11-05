"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            cur, tmp, cnt = s[0], '', 0
            for next in s:
                if cur == next:
                    cnt += 1
                else:
                    tmp += str(cnt) + cur
                    cur = next
                    cnt = 1
            s = tmp + str(cnt) + cur
        return s

s = Solution()
s.countAndSay(5)
