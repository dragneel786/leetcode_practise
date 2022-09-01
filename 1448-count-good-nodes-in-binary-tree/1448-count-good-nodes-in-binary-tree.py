# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def counts_good(root, value = -inf):
            nonlocal counts
            if(not root):
                return
            
            if(root.val >= value):
                counts += 1
            
            counts_good(root.left, max(value, root.val))
            counts_good(root.right, max(value, root.val))
        
        counts = 0
        counts_good(root)
        return counts