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
        if(not head):
            return None
        
        node = head
        while(node):
            temp = node.next
            node.next = Node(node.val)
            node.next.next = temp
            node = temp
        
        nHead = head.next
        while(True):
            if(head.random):
                head.next.random = head.random.next
            temp = head.next.next
            if(not temp):
                return nHead
            head.next.next = temp.next
            head = temp
        