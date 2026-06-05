# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        visited = dict()
        curr = head
        while curr.next:
            if curr not in visited:
                visited[curr] = curr.next
            elif curr in visited:
                return True
            curr = curr.next

        return False