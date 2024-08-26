"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        node_values = []
        for ch in (root.children or []):
            node_values.extend(self.postorder(ch))
            
        return node_values + [root.val]
            