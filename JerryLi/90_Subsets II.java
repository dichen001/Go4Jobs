/*
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
*/

public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
    	/*
    	Solution in Discussion:
    	deal with duplicate elements when backtracking
    	*/
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        result.add(new LinkedList<Integer>());
        Arrays.sort(nums);
        
        for (int i=0; i<nums.length; i++){
            int duplicate = 0;
            while ((i+1)<nums.length && nums[i]==nums[i+1]) {
                i++;
                duplicate++;
            }
            int curSize = result.size();
            for (int j=0; j<curSize; j++){
                List<Integer> tmp = new LinkedList<Integer>(result.get(j));
                for (int k=0; k<=duplicate; k++){
                    tmp.add(nums[i]);
                    result.add(new LinkedList<Integer>(tmp));
                }
            }
        }
        return result;
    }
}