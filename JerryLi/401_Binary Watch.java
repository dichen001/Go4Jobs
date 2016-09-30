/*
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
*/

public class Solution {
    public List<String> readBinaryWatch(int num) {
        /*
        Simple solution in Discussion:
        use Integer.bitCount() to convert int to bits
        */
        List<String> result = new ArrayList<String>();
        for (int hour=0; hour < 12; hour++){
            for (int minute=0; minute<60; minute++){
                if (Integer.bitCount(hour)+Integer.bitCount(minute)==num)
                    result.add(String.format("%d:%02d", hour, minute));
            }
        }
        return result;
    }
}
