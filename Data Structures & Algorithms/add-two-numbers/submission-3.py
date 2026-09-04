# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        carry = 0

        while l1 or l2 or carry:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            sum = l1_val + l2_val + carry
            carry = 1 if sum >= 10 else 0
            digit = sum - 10 if sum >= 10 else sum

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = None if not l1 else l1.next
            l2 = None  if not l2 else l2.next
        
        return dummy.next
