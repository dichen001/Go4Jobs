class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.dfs(candidates,target,0,[],res)
        return res
    def dfs(self,candidates,target,index,list,res):
        if target<0:
            return
        elif target==0:
            res.append(list)
            return
        for i in xrange(index,len(candidates)):
            self.dfs(candidates,target-candidates[i],i,list+[candidates[i]],res)