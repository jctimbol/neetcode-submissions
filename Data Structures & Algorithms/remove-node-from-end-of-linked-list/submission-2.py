# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        nodes = 0
        curr = head

        while curr:
            nodes += 1
            curr = curr.next
        
        index = nodes - n
        
        if index == 0:
            if not head.next:
                return None
            else:
                return head.next
        
        prev, curr = head, head.next
        curr_idx = 1

        while curr:
            if curr_idx == index:
                prev.next = curr.next
                break

            if curr_idx > 0:
                prev = curr

            curr = curr.next
            #print(prev.val, curr.val)
            curr_idx += 1
        
        return head if not None else prev

            