class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, stack, sign = 0, [], 1
        queue = [c for c in s][::-1]
        while queue:
            c = queue.pop()
            if c == ' ':
                continue
            elif c == '(':
                stack.append((ans, sign))
                ans, sign = 0, 1
            elif c == ')':
                prev, sign = stack.pop()
                ans = prev + sign * ans
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            else:
                tmp = [c]
                while queue and queue[-1].isdigit():
                    tmp.append(queue.pop())
                ans += sign * int(''.join(tmp))
        return ans


s = Solution()
s.calculate("1-(5)")