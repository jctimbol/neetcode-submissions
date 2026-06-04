# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        prev = head
        curr = head.next
        after = curr.next
        
        head.next = None
        head = None

        while(after):
            curr.next = prev
            prev = curr
            curr = after
            after = after.next
            
        curr.next = prev
        
        return curr