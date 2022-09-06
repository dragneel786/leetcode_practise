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
                return None
            
            root.left = prune_tree(root.left)
            root.right = prune_tree(root.right)
            
            if(root.val == 1 or root.left or root.right):
                return root
            
            return None
        
        
        return root if(prune_tree(root)) else None
        
        