class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        flag=1
        while x//flag>=10:
            flag=flag*10
        while x>0:
            l=x//flag
            r=x%10
            if l!=r:
                return False
            x=(x%flag)//10
            flag=flag//100
        return True