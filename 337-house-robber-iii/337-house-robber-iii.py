# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def robIt(root):
            if(not root):
                # with Robbery, without Roberry.
                return 0, 0
            
            left = robIt(root.left)
            right = robIt(root.right)
            withRoot = left[1] + right[1] + root.val
            withoutRoot = max(left) + max(right)
            return withRoot, withoutRoot
            
        return max(robIt(root))