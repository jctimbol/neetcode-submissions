# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        curr = None
        compare = None
        switch = None

        if list1.val <= list2.val:
            head = list1
            curr = list1
            compare = list2
        else:
            head = list2
            curr = list2
            compare = list1


        while curr.next and compare:
            if curr.next.val > compare.val:
                switch = curr.next
                curr.next = compare
                compare = switch 
            curr = curr.next
        
        if compare:
            curr.next = compare

        return head
