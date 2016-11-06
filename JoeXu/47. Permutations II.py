class Solution(object):
    '''
    compared to previous one, ad a judgement
    '''
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=len(nums)
        res=[]
        if l==0:
            return []
        if l==1:
            return [[nums[0]]] 
        nums.sort()
        temp=None
        for i in range(l):
            if nums[i]==temp:
                continue
            temp=nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res
        