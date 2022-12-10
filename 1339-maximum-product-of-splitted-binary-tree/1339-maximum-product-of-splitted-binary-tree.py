# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def sum_root(node):
            if(not node):
                return 0
            
            left = sum_root(node.left)
            right = sum_root(node.right)
            return left + right + node.val
        
        
        def postorder(node):
            nonlocal maxprod, sums
            if(not node):
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)
            maxprod = max(maxprod, left * (sums - left), right * (sums - right))
            return left + right + node.val
        
        sums = sum_root(root)
        maxprod = 0
        postorder(root)
        return maxprod % (10 ** 9 + 7)
        