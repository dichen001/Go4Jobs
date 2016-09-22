/*
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
*/

public class Solution {
    public void rotate(int[] nums, int k) {
        int moves = k % nums.length; # Rotation offset by length of array
        if (moves == 0) return;
        int[] tmp = new int[moves];
        int lastIndex = nums.length-1;
        int t = moves;
        while(t>0){
            tmp[t-1] = nums[lastIndex+t-moves];
            t--;
        }
        for (int i=lastIndex; i>moves-1; i--){
            nums[i] = nums[i-moves];
        }
        for (int i=0; i<moves; i++){
            nums[i] = tmp[i];
        }
    }
}