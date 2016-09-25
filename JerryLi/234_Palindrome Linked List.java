/*
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head==null || head.next==null) return true;
        /*
        Two pointers: fast run 2 step, and slow run 1 step;
        when fast run over the list, slow just reach the middle;
        rev pointer follow slow pointer, and reverse the direction of list link.
        */
        ListNode rev=null, fast=head, slow=head;
        boolean result = true;
        while (fast!=null && fast.next!=null){
            fast = fast.next.next;
            if (rev == null){
                rev = slow;
                slow = slow.next;
            } else {
                ListNode tmp = slow;
                slow = slow.next;
                tmp.next = rev;
                rev = tmp;
            }
        }
        if (fast != null) slow = slow.next;
        while (slow != null){
            if (slow.val != rev.val){
                result = false;
                break;
            }
            slow = slow.next;
            rev = rev.next;
        }
        return result;
    }
}