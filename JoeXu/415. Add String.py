class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1=len(num1)
        l2=len(num2)
        n1=0
        n2=0
        for i in range(l1):
            n1+=int(num1[i])*10**(l1-i-1)
            
        for j in range(l2):
            n2+=int(num2[j])*10**(l2-j-1)
            
        return str(n1+n2)