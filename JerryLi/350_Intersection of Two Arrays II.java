/*
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
*/

public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        /*
        HashMap/Dictionary:
        Put the each array into a Map<value, times==0>;
        Check the intersection segments in this Map by taking the min times of each element appearance.
        */
        if (nums1.length==0 || nums2.length==0) return new int[0];
        
        Map<Integer, Integer> dict1 = new HashMap<Integer, Integer>();
        Map<Integer, Integer> dict2 = new HashMap<Integer, Integer>();
        
        for (int i=0; i<nums1.length; i++){
            if (dict1.get(nums1[i])==null)
                dict1.put(nums1[i], 1);
            else
                dict1.put(nums1[i], dict1.get(nums1[i])+1);
        }
        for (int i=0; i<nums2.length; i++){
            if (dict2.get(nums2[i])==null)
                dict2.put(nums2[i], 1);
            else
                dict2.put(nums2[i], dict2.get(nums2[i])+1);
        }
        
        List<Integer> intersection = new LinkedList<Integer>();
        for (int item: dict1.keySet()){
            if (dict2.containsKey(item)){
                int count = Math.min(dict2.get(item), dict1.get(item));
                for (int i=0; i<count; i++)
                    intersection.add(item);
            }
        }
        
        int[] result = new int[intersection.size()];
        for (int i=0; i<intersection.size(); i++)
            result[i] = intersection.get(i);
        
        return result;
    }
}