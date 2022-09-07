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
            
            left = construct_string(root.left)
            right = construct_string(root.right)
            
            if(left or right): left = f'({left})'
            if(right): right = f'({right})'
            
            return str(root.val) + left + right
            
        return construct_string(root)
            
            
            