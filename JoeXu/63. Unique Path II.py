class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==0 or n==0:
            return 0
        else:
            list=[[0 for i in range(n)]for j in range(m)]
            for i in range(m):
                if obstacleGrid[i][0]==0:
                    list[i][0]=1
                else:
                    list[i][0]=0
                    break
            for i in range(n):
                if obstacleGrid[0][i]==0:
                    list[0][i]=1
                else:
                    list[0][i]=0
                    break
            for i in range(1,m):
                for j in range(1,n):
                    if obstacleGrid[i][j]==1: list[i][j]=0
                    else:
                        list[i][j]=list[i-1][j]+list[i][j-1]
            return list[m-1][n-1]