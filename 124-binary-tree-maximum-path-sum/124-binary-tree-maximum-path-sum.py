# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def path_sums(root):
            nonlocal max_path
            if(not root):
                return 0
        
            left = max(path_sums(root.left), 0)
            right = max(path_sums(root.right), 0)
            
            ret = root.val+ max(left, right)
            max_path = max(max_path, left + right + root.val)
            return ret
        
        max_path = -inf
        path_sums(root)
        return max_path
            
            