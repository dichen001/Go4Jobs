/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

public class Solution {
    public String convert(String s, int numRows) {
        /*
        Solution in Discussion:
        Use StringBuffer for dynamical memory allocation.
        */
        char[] schar = s.toCharArray();
        int size = schar.length;
        int row=0, index=0;
        StringBuffer[] buffers = new StringBuffer[numRows];
        for (int i=0; i<numRows; i++) buffers[i] = new StringBuffer();
        
        while (index < size){
            for (row=0; row<numRows && index<size; row++){
                buffers[row].append(schar[index++]);
            }
            for (row=numRows-2; row>0 && index<size; row--){
                buffers[row].append(schar[index++]);
            }
        }
        
        for (row=1; row<numRows; row++) buffers[0].append(buffers[row]);
        return buffers[0].toString();
    }
}