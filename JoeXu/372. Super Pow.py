class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        #c mod m = (a ⋅ b) mod m  = [(a mod m) ⋅ (b mod m)] mod m
        res=1
        c=1337
        for i in b[::-1]:
            res = res * a ** i % c
            a = a ** 10 % c
        return res