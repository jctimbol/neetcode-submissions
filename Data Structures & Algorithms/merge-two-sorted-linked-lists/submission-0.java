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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
       ListNode curr;
       ListNode l1;
       ListNode l2;
        ListNode head;
       
       if(list1 == null) {
        return list2;
       }
       if(list2 == null) {
        return list1;
       }
       
       if(list1.val < list2.val) {
        curr = list1;
        head = list1;
        l1 = curr.next;
        l2 = list2;
       }
       else {
        curr = list2;
        head = list2;
        l2 = curr.next;
        l1 = list1;
       }

       while(l1 != null && l2 != null) {
        if(l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        }
        else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
       }

       while(l1 != null) {
        curr.next = l1;
        l1 = l1.next;
        curr = curr.next;
       }
       while(l2 != null) {
        curr.next = l2;
        l2 = l2.next;
        curr = curr.next;
       }
       
        return head;
    }
}