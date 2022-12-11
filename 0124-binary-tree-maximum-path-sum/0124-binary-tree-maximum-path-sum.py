# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            nonlocal ans
            if(not node):
                return -inf
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            ans = max(ans, left + node.val, right + node.val,\
                      left + right + node.val, node.val)
            return max(max(left, right) + node.val, node.val)
        
        
        ans = -inf
        dfs(root)
        return ans