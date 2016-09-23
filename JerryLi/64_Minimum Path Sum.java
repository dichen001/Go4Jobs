/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*/

public class Solution {
    public int minPathSum(int[][] grid) {
        /*
        DP:
        i, j from (0,0) to (n,n)
        minPath = min(sum[i][j-1]+grid[i][j], sum[i-1][j]+grid[i][j])
        */
        int m = grid.length, n = grid[0].length;
        int[][] minSum = new int[m][n];
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (i==0 && j==0)
                    minSum[i][j] = grid[i][j];
                else if (i==0 && j>0)
                    minSum[i][j] = minSum[i][j-1] + grid[i][j];
                else if (j==0 && i>0)
                    minSum[i][j] = minSum[i-1][j] + grid[i][j];
                else
                    minSum[i][j] = Math.min(minSum[i-1][j]+grid[i][j], minSum[i][j-1]+grid[i][j]);
            }
        }
        return minSum[m-1][n-1];
    }
}