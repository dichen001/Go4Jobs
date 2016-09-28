/*
Write a function to find the longest common prefix string amongst an array of strings.
*/

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        /*
        Solution in discussion:
        First sort string array by letter from head to tail.
        Then compare first with last element in sorted string array.
        */
        if (strs==null || strs.length==0) return "";
        Arrays.sort(strs);
        StringBuilder result = new StringBuilder();
        
        char[] first = strs[0].toCharArray();
        char[] last = strs[strs.length-1].toCharArray();
        
        for (int i=0; i<first.length; i++){
            if (last.length > i && last[i]==first[i]){
                result.append(first[i]);
            } else {
                break;
            }
        }
        return result.toString();
    }
}