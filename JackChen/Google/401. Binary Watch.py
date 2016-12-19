"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
Show Company Tags
Show Tags
Show Similar Problems
"""
hours = {
            0:[0],
            1:[2**i for i in range(4)],
            2:[2**i + 2**j for i in range(3) for j in range(i+1, 4) if 2**i + 2**j < 12],
            3:[2**i ^ 15 for i in range(4) if 2**i ^ 15 < 12]
                }
minutes = {
            0:[0],
            1:[2**i for i in range(6)],
            2:[2**i + 2**j for i in range(5) for j in range(i+1, 6) if 2**i + 2**j],
            3:[2**i + 2**j + 2**k for i in range(4) for j in range(i+1, 5) for k in range(j+1,6)],
            4:[(2**i + 2**j) ^ 63 for i in range(5) for j in range(i+1, 6) if (2**i + 2**j) ^ 63 < 60],
            5:[2**i ^ 63 for i in range(6) if 2**i ^ 63 < 60]
            }
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # top solusion
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]


        # my complicated solusion
        ans = []
        for h in range(num+1):
            m = num-h
            if h in range(4) and m in range(6):
                hour = [str(x) for x in hours[h]]
                minute = [str(x) if x > 9 else '0' + str(x) for x in minutes[m]]
                ans += [h + ':' + m for h in hour for m in minute]
        return ans



s = Solution()
s.readBinaryWatch(3)
