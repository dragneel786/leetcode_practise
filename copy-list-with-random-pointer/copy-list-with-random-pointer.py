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
        h1 = head
        node_map = dict()
        new_head = h2 = Node(-1)
        
        while(h1):
            h2.next = Node(h1.val)
            node_map[h1] = h2.next
            h1 = h1.next
            h2 = h2.next
        
        
        h1 = head
        h2 = new_head.next
        while(h1):
            if(h1.random):
                h2.random = node_map[h1.random]
            h1 = h1.next
            h2 = h2.next
        
        return new_head.next
        