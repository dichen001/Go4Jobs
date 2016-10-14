/*
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
*/

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        /*
        Solution in Discussion:
        Use two pointers to measure the length and update the sum
        */
        if (nums==null || nums.length==0) return 0;
        int start=0, end=0, minLen=Integer.MAX_VALUE, sum=0;
        while (end<nums.length){
            while (end<nums.length && sum<s) sum += nums[end++];
            if (sum < s) break;
            while (start<end && sum>=s) sum -= nums[start++];
            minLen = Math.min(minLen, end-start+1);
        }
        return minLen==Integer.MAX_VALUE? 0: minLen;
    }
}