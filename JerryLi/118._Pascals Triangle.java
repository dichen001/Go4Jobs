/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

// Naive solution using formula of Pascal's Triangle (wiki)

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0) return new LinkedList<List<Integer>>();
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        result.add(new LinkedList<Integer>()); // 1st level
        result.get(0).add(1);
        if (numRows == 1) return result;
        result.add(new LinkedList<Integer>()); // 1st level
        result.get(1).add(1);
        result.get(1).add(1);
        for (int i=2; i<numRows; i++){
            int j=1;
            result.add(new LinkedList<Integer>());
            result.get(i).add(1);
            while(j<i){
                result.get(i).add(result.get(i-1).get(j-1) + result.get(i-1).get(j));   
                j++;
            }
            result.get(i).add(1);
        }
        return result;
    }
}