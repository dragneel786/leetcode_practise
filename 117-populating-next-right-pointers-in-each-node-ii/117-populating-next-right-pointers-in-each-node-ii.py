"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(not root):
            return 
        
        if(root.left):
            if(root.right):
                root.left.next = root.right
            else:
                root.left.next = self.getNext(root.next)
            
        if(root.right):
            root.right.next = self.getNext(root.next)
        
        self.connect(root.right)
        self.connect(root.left)
        return root
    
    def getNext(self, root):
        while(root):
            if(root.left):
                return root.left
            if(root.right):
                return root.right
            root = root.next
        return None
        
        
            
            
            
            
            
        
                
        
        
                