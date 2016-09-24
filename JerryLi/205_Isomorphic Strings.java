/*
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
*/


public class Solution {
    public boolean isIsomorphic(String s, String t) {
        /*
        Encode char into integer indexed by order, then determine pattern by the codes.
        */
        char[] schar = s.toCharArray();
        char[] tchar = t.toCharArray();
        
        if (schar.length != tchar.length) return false;
        
        Map<Character, Integer> sm = new HashMap<Character, Integer>();
        Map<Character, Integer> tm = new HashMap<Character, Integer>();
        
        int[] scode = new int[schar.length];
        int[] tcode = new int[tchar.length];
        
        int shash = -1, thash=-1;
        boolean result = true;
        for (int i=0; i<schar.length; i++){
            if (!sm.containsKey(schar[i])){
                sm.put(schar[i], ++shash);
                scode[i] = shash;
            } else {
                scode[i] = sm.get(schar[i]);
            }
            if (!tm.containsKey(tchar[i])){
                tm.put(tchar[i], ++thash);
                tcode[i] = thash;
            } else {
                tcode[i] = tm.get(tchar[i]);
            }
            if (scode[i] != tcode[i]){
                result = false;
                break;
            }
        }
        
        return result;
    }
}

/*
//Solution in Discussion

public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> s2t = new HashMap<>();
        Map<Character, Character> t2s = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            s2t.put(s.charAt(i), t.charAt(i));
            t2s.put(t.charAt(i), s.charAt(i));
        }
        
        for(int i =0; i < s.length(); i++){
            if(s2t.get(s.charAt(i)) != t.charAt(i)) return false;
            if(t2s.get(t.charAt(i)) != s.charAt(i)) return false;
        }
        
        return true;
    }

*/