# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []
        n = 0
        while curr:
            nodes.append(curr)
            curr = curr.next
            n += 1

        for node in nodes:
            node.next = None
                            
        l = 0
        r = n-1

        while l < r:
            nodes[l].next = nodes[r]
            if l+1 >= r:
                break
            nodes[r].next = nodes[l+1]
            l += 1
            r -= 1
        