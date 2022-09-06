# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def prune_tree(root):
            if(not root):
                return False
            
            left = prune_tree(root.left)
            right = prune_tree(root.right)
            
            if(not left):
                root.left = None
            
            if(not right):
                root.right = None
            
            return left or right or root.val == 1
        
        
        return root if(prune_tree(root)) else None
        
        