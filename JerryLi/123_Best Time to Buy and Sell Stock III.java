/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
*/

public class Solution {
    public int maxProfit(int[] prices) {
        /*
        Solution in Discussion:
        DP:
        check profit by comparing current price with previous cost and profit.
        */
        int maxProfit1 = 0, maxProfit2 = 0;
        int lowestPrice1 = Integer.MAX_VALUE, lowestPrice2 = Integer.MAX_VALUE;    
        for (int p: prices){
            maxProfit2 = Math.max(maxProfit2, p-lowestPrice2);
            lowestPrice2 = Math.min(lowestPrice2, p-maxProfit1);
            maxProfit1 = Math.max(maxProfit1, p-lowestPrice1);
            lowestPrice1 = Math.min(lowestPrice1, p);
        }
        return maxProfit2;
    }
}