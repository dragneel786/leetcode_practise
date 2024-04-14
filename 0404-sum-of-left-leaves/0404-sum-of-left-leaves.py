# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sums(node, is_left = False):
            if(not node):
                return 0
            
            if(not node.left and \
               not node.right and is_left):
                return node.val
            
            return sums(node.left, True) \
        + sums(node.right, False)
            
        return sums(root)
        