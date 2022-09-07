# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def construct_string(root):
            if(not root): return ''
            
            if(not root.left and not root.right):
                return str(root.val) + ''
            
            if(not root.right):
                return str(root.val) + f'({construct_string(root.left)})'
            
            return str(root.val) + f'({construct_string(root.left)})({construct_string(root.right)})'
        return construct_string(root)
            
            
            