class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        f=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+f==10:
                digits[i]=0
                f=1
            else:
                digits[i]=digits[i]+f
                f=0
        if f==1:
            digits.insert(0,1)
        return digits