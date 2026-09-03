# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2

        while ptr1 and ptr2:
            sum = ptr1.val + ptr2.val
            if sum > 9:
                ptr2.val = sum - 10
                if ptr2.next:
                    ptr2.next.val += 1
                else:
                    new = ListNode(val=1)
                    ptr2.next = new
            else:
                ptr2.val = sum

            if ptr1.next and not ptr2.next:
                ptr2.next = ptr1.next
                break

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr2:
            if ptr2.val > 9:
                ptr2.val -= 10
                new = ListNode(val=1)
                ptr2.next = new
            ptr2 = ptr2.next

        return l2