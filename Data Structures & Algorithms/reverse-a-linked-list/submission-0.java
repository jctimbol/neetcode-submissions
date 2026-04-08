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
    public ListNode reverseList(ListNode head) {
        ListNode curr = null;
        ListNode oldPrev;
        ListNode oldNext;

        if(head != null) {
        curr = head;
        oldPrev = curr;
        oldNext = curr.next;

        curr.next = null;
        
        

        while(oldNext != null) {
            curr = oldNext;
            oldNext = curr.next;
            curr.next = oldPrev;
            oldPrev = curr;
        }
        }
        return curr;
    }
}
