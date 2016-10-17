/*
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
*/

public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        /*
        Solution in Discussion:
        The key point is that it is not doing hash, it is doing the exact coding of a 10-letter sequence into a 4-bytes number, which is simply not possible for any generic string, but is possible for strings in this problem because they can have only 4 differfent characters.
        */
        List<String> result = new ArrayList<String>();
        if (s==null || s.length()==0) return result;
        Set<Integer> words = new HashSet<Integer>();
        Set<Integer> doublewords = new HashSet<Integer>();
        char[] encode = new char[26]; // encode of the 4 letters
        encode['C'-'A'] = 1;
        encode['G'-'A'] = 2;
        encode['T'-'A'] = 3;
        int value = 0;
        for (int i=0; i<s.length(); i++){
            value <<= 2;
            value |= encode[s.charAt(i)-'A'];
            value &= 0xfffff;
            if (i<9)
                continue;
            else {
                if (!words.add(value) && doublewords.add(value)){
                    result.add(s.substring(i-9, i+1));
                }
            }
        }
        return result;
    }
}