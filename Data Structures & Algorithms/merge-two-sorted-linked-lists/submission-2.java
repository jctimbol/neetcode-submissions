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
        if(list1 == null && list2 == null) return null;
        if(list1 != null && list2 == null) return list1;
        if(list1 == null && list2 != null) return list2;

        ListNode head;
        ListNode ptr;
        ListNode l1;
        ListNode l2;

        if(list1.val < list2.val) {
            ptr = list1;
            l1 = ptr.next;
            l2 = list2;
        }
        else {
            ptr = list2;
            l1 = list1;
            l2 = ptr.next;
        }
        head = ptr;
        while(l1 != null && l2 != null) {
            if(l1.val < l2.val) {
                ptr.next = l1;
                l1 = l1.next;
            }
            else {
                ptr.next = l2;
                l2 = l2.next;
            }
            ptr = ptr.next;
        }

        if (l1 != null) {
            ptr.next = l1;
        }
        if(l2 != null) {
            ptr.next = l2;
        }

        return head;

    }
}