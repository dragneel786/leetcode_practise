# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def values(node):
            if not node:
                return []
            
            if node.left == node.right == None:
                return [node.val]
                
            left = values(node.left)
            right = values(node.right)
            return left + right
        
        return values(root1) == values(root2)