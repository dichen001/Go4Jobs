"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.
Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0;
        l, num, sign =list(s), 0, '+'
        stack = []
        for idx,i in enumerate(l):
        	if i.isdigit():
        		num = num*10+ord(i)-ord('0')
        	if (i in ('+','-','*','/')) or idx == len(l) - 1:
        		if sign=='+':
        			stack.append(num)
        		if sign=='*':
        			stack.append(stack.pop() * num)
        		if sign=='-':
        			stack.append(-num)
        		if sign=='/':
        		    t = stack.pop()
        		    t = t / num if t > 0 else -(-t / num)
       			    stack.append(t)
        		sign = i
        		num=0
        r = 0
        for n in stack:
            r += n
        return r
