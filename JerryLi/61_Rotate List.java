/*
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    public ListNode rotateRight(ListNode head, int k) {
        /*
        Solution in Discussion:
        1. Connect head and tail to form a circular list;
        2. Rotate from head to (size - k)%size nodes;
        3. Break the circular list at head node.
        */
        if (head==null || head.next==null || k==0) return head;
        int size = 1;
        ListNode fast = head;
        while (fast.next != null) {
            fast = fast.next;
            size++;
        }
        fast.next = head;
        int steps = size - (k % size);
        while (steps-- > 0){
            fast = fast.next;
        }
        head = fast.next;
        fast.next = null;
        return head;
    }
}