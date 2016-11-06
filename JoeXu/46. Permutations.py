class Solution(object):
    def permute(self, nums):
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
        for i in range(l):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res
'''
another beat 98% solution:
class Solution(object):
    def recurse(self, nums, ans, trace=[]):
        if nums == []:
            ans.append(trace)
            return
        for i in range(len(nums)):
            tmp = nums[i]
            nums.pop(i)
            self.recurse(nums, ans, trace + [tmp])
            nums.insert(i, tmp)
    def permute(self, nums):
        ans = []
        self.recurse(nums, ans)
        return ans
'''