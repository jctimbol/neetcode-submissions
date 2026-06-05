# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        visited = set()
        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
            elif curr in visited:
                return True
            curr = curr.next

        return False