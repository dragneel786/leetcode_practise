# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        
        def add_to_depth(node, val, dep):
            if(not node):
                return 
            
            if(dep == 1):
                left, right = node.left, node.right
                node.left = TreeNode(val, left=left)
                node.right = TreeNode(val,right=right)
                return
            
            add_to_depth(node.left, val, dep - 1)
            add_to_depth(node.right, val, dep - 1)
        
        dummy_root = TreeNode()
        dummy_root.left = root
        
        add_to_depth(dummy_root, val, depth)
        
        return dummy_root.left
        
        