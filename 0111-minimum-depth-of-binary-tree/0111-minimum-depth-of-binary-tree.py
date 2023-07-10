# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def min_d(root):
            if(not root):
                return inf

            if(not root.left and not root.right):
                return 1

            left = 1 + min_d(root.left)
            right = 1 + min_d(root.right)
            return min(left, right)
        
        if(root):
            return min_d(root)
        
        return 0