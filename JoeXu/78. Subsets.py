class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth,start,valuelist):
            res.append(valuelist)
            if depth==len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,valuelist+[nums[i]])
        res=[]
        nums.sort()
        dfs(0,0,[])
        return res