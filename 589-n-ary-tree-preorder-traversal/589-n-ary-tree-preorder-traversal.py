"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if(root):
            res.append(root.val)
            for c in root.children:
                res.extend(self.preorder(c))
        return res