# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        
        def get_min_diff(node):
            nonlocal ans, prev
            if(not node):
                return
            
            get_min_diff(node.left)
            if(prev != -1):
                ans = min(ans, abs(node.val - prev))
            prev = node.val
            get_min_diff(node.right)
            
        ans, prev = inf, -1
        get_min_diff(root)
        return ans