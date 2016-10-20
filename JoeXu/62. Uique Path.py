class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        if m==1 or n==1:
            return 1
        else:
            list=[[0 for i in range(n)]for j in range(m)]
            for i in range(m):
                list[i][0]=1
            for i in range(n):
                list[0][i]=1
            for i in range(1,m):
                for j in range(1,n):
                    list[i][j]=list[i-1][j]+list[i][j-1]
            return list[m-1][n-1]