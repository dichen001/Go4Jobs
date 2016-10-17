/*
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

*/

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        /*
        Solution in Discussion:
        Bucket sort by element frequency
        */
        List<Integer> result = new ArrayList<>();
        if (nums==null || nums.length==0) return result;
        Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
        List<Integer>[] bucket = new List[nums.length+1];
        for (int n: nums){
            counter.put(n, counter.getOrDefault(n, 0)+1);
        }
        for (int key: counter.keySet()){
            int ct = counter.get(key);
            if (bucket[ct] == null)
                bucket[ct] = new ArrayList<Integer>();
            bucket[ct].add(key);
        }
        for (int i=nums.length; i>=0 && result.size()<k; i--){
            if (bucket[i] != null){
                for (int j=0; j<bucket[i].size() && result.size()<k; j++)
                    result.add(bucket[i].get(j));
            }
        }
        return result;
    }
}