# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def tot_count(node):
            nonlocal res
            if(not node):
                return 0, 0
            
            left, lc = tot_count(node.left)
            right, rc = tot_count(node.right)
            tot = left + right + node.val
            tc = lc + rc + 1
            if(tot // tc == node.val):
                res += 1
            
            return tot, tc
        
        res = 0
        tot_count(root)
        return res