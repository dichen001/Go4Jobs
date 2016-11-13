class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=len(height)
        maxheight=[0 for i in range(l)]
        leftmax=0
        rightmax=0
        res=0
        for i in range(l):
            if height[i]>leftmax:
                leftmax=height[i]
            maxheight[i]=leftmax
        
        for i in reversed(range(l)):
            if height[i]>rightmax:
                rightmax=height[i]
            if min(rightmax,maxheight[i])-height[i]>0:
                res+=min(rightmax,maxheight[i])-height[i]
        return res