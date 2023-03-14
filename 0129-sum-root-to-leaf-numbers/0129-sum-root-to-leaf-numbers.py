# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def get_sum(node, val = 0):
            nonlocal sums
            if(not node):
                return 
            
            value = val * 10  + node.val
            if(not node.left and not node.right):
                sums += value
                return
            get_sum(node.left, value)
            get_sum(node.right, value)
        
        sums = 0
        get_sum(root)
        return sums