# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def sum_it(root):
            nonlocal sums
            if(not root):
                return
            
            if(low <= root.val <= high):
                sums += root.val
            
            if(root.val > low):
                sum_it(root.left)
            
            if(root.val < high):
                sum_it(root.right)
        
        sums = 0
        sum_it(root)
        return sums
        