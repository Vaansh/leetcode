/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int res = 0;

        // [1, 0, 1] -> 2^2 * 1 + 2^1 * 0 + 2^0 * 1
        //           -> 0 * 2 + 1, 1 * 2 + 0, 2 * 2 + 1
        while (head != null) {
            res = (res * 2) + head.val;
            head = head.next;
        }
        
        return res;
    }
}