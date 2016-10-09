import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #algo: http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
        p = random.choice(nums)
        A1=[]
        A2=[]
        for n in nums:
            if n > p:
                A1.append(n)
            elif n < p:
                A2.append(n)
        if k <= len(A1):
            return self.findKthLargest(A1,k)
        elif k>len(nums)-len(A2):
            return self.findKthLargest(A2,k-(len(nums)-len(A2)))
        else:
	        return p
