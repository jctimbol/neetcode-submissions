# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, curr, old_next = None, head, head.next

        while old_next:
            curr.next = prev
            prev = curr
            curr = old_next
            old_next = curr.next

        curr.next = prev

        return curr