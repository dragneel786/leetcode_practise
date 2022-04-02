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
        
        hashIt = dict()
        newHead = Node(head.val)
        hashIt[head] = newHead
        mhead = head.next
        chead = newHead
        while(mhead):
            chead.next = Node(mhead.val)
            hashIt[mhead] = chead.next
            chead = chead.next
            mhead = mhead.next
        
        while(head):
            if(head.random):
                hashIt[head].random = hashIt[head.random]
            head = head.next
        
        return newHead
        