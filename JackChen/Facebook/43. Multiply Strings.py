class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = 0
        for i, c2 in enumerate(num2[::-1], 1):
            flag, tmp = 0, []
            for j, c1 in enumerate(num1[::-1], 1):
                c1 = num1[-j]
                tmp += [str((int(c1) * int(c2) + flag) % 10)]
                flag = (int(c1) * int(c2) + flag) / 10
            if flag:
                tmp.append(str(flag))
            ans += int(''.join(tmp[::-1])) * 10 ** (i - 1)
        return str(ans)