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

        new_head = Node(head.val)
        new_curr = new_head

        #track randoms
        original_to_new = {None: None}

        #set up nexts
        curr = head

        while curr:
            original_to_new[curr] = new_curr

            if curr.next:
                new_curr.next = Node(curr.next.val)
            curr = curr.next
            new_curr = new_curr.next


        #set up randoms
        curr = head 
        new_curr = new_head

        while curr:
            original_random = curr.random
            new_curr.random = original_to_new[original_random]

            curr = curr.next
            new_curr = new_curr.next
        
        return new_head
            