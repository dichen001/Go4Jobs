"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, num, sign = 0, 0, 1
        stack = []
        for i in s:
        	if i.isdigit():
        		num = num*10+ord(i)-ord('0')
        	if i == '+':
    			result += sign*num
    			num, sign = 0, 1
    		if i == '-':
    			result += sign*num
    			num, sign = 0, -1
        	if i == '(':
        	    stack.extend([result, sign])
        	    result, sign = 0, 1
        	if i == ')':
        	    result += sign*num
        	    result *= stack.pop()
        	    result += stack.pop()
        	    num=0
        return result if not num else result + sign * num
