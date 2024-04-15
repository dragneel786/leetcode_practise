# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def sums(node, val=0):
            nonlocal res
            if(not node):
                return
            
            new_val = (val * 10) + node.val
            if(not node.left and not node.right):
                res += new_val
                return
            
            val1 = sums(node.left, new_val)
            val2 = sums(node.right, new_val)
            
        
        res = 0
        sums(root)
        return res
            
            
        