# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def all_leafs(node):
            if(not node):
                return []
            
            if(not node.left and not node.right):
                return [node.val]
            
            left = all_leafs(node.left)
            right = all_leafs(node.right)
            return left + right
        
        
        return all_leafs(root1) == all_leafs(root2)
            