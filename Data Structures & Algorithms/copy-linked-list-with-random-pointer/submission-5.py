"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}

        old_curr = head

        new_curr = Node(head.val)
        new_head = new_curr

        #pass 1: set up nexts and dict
        while old_curr:
            if not old_curr.next:
                new_curr.next = None
            else:
                new_curr.next = Node(old_curr.next.val)
            
            old_to_new[old_curr] = new_curr

            old_curr = old_curr.next
            new_curr = new_curr.next
        
        old_curr = head
        new_curr = new_head

        while old_curr:
            if not old_curr.random:
                new_curr.random = None

            else:
                new_curr.random = old_to_new[old_curr.random]

            old_curr = old_curr.next
            new_curr = new_curr.next
        

        return new_head