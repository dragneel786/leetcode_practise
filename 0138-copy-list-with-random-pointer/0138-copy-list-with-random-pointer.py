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
        copy_head = Node(0)
        lookup_map = {}
        curr = head
        new_curr = copy_head
        while(curr):
            new_node = Node(curr.val)
            lookup_map[curr] = new_node
            new_curr.next = new_node
            new_curr = new_curr.next
            curr = curr.next
        
        curr = head
        new_curr = copy_head.next
        while(curr):
            if(curr.random):
                new_curr.random = lookup_map[curr.random]
            new_curr = new_curr.next
            curr = curr.next
        
        return copy_head.next
            
            
        
            
            
        