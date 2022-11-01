"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = deque([root])
        res = []
        
        while(stack):
            if(not stack[-1]):
                stack.pop()
                continue
                
            if(not stack[-1].children):
                res.append(stack.pop().val)
                continue
            
            node = stack[-1]
            for child in reversed(node.children):
                stack.append(child)
            
            node.children = None
        
        return res
                
                
            
        