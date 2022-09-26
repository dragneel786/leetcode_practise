# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            return -1 if(not node) else 1 + height(node.left)
        
        
        h = height(root)
        if(h < 0):
            return 0
        
        return (1 << h) + self.countNodes(root.right)\
    if(height(root.right) == h - 1) else (1 << h-1) + self.countNodes(root.left) 
        