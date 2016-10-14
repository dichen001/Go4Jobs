/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/

public class Solution {
    public void nextPermutation(int[] nums) {
        /*
        Solution in Discussion:
        1. Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. So, elements from num[i] to num[n-1] is reversely sorted.
        2. To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with the smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 121543321, we want to swap the '1' at position 2 with '2' at position 7.
        3. The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the num[i,n-1]
        */
        if (nums==null || nums.length<=1) return;
        boolean possible = false;
        int index = nums.length-2;
        for (; index>=0; index--){
            if (nums[index]<nums[index+1]) {
                possible = true;
                break;
            }
        }
        if (!possible){
            int left=-1, right=nums.length;
            while (++left < --right){
                swap(nums, left, right);
            }
        } else {
            for (int i=nums.length-1; i>index; i--){
                if (nums[index] < nums[i]) {
                    swap(nums, index, i);
                    break;
                }
            }
            Arrays.sort(nums, index+1, nums.length);
        }
    }
    
    private void swap(int[] arr, int i, int j){
        arr[i] ^= arr[j];
        arr[j] ^= arr[i];
        arr[i] ^= arr[j];
    }
}