/*
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
*/

public class Solution {
    public int maxProduct(int[] nums) {
    	/*
    	Solution in Discussion:
    	swap min and max when coming to the negative element
    	*/
        int max=1, min=1, result=Integer.MIN_VALUE;
        for (int i=0; i<nums.length; i++){
            if (nums[i] < 0){
                int tmp = max;
                max = min;
                min = tmp;
            }
            int tmax = Math.max(nums[i], nums[i]*max);
            int tmin = Math.min(nums[i], nums[i]*min);
            max = tmax;
            min = tmin;
            result = Math.max(result, max);
        }
        return result;
    }
}