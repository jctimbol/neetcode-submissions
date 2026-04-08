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
    public boolean hasCycle(ListNode head) {
        ListNode curr = head;
        HashMap<Integer, Integer> nodes = new HashMap<>();

        while(curr.next != null) {
           if(nodes.containsKey(curr.val) && nodes.containsValue(curr.next.val)) {
                return true;
            }
            nodes.put(curr.val, curr.next.val);
            curr = curr.next;
        }
        return false;
    }
}
