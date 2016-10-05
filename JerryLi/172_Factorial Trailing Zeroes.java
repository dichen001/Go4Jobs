/*
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity
*/

public class Solution {
    public int trailingZeroes(int n) {
        /*
        Solution in Discussion:
        count factor of 5 to determine number of 10 powers
        */
        if (n==0) return 0;
        int count = 0;
        while (n>1){
            count += n/5;
            n /= 5;
        }
        return count;
    }
}