# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
                
        def sumed(node, p, gp):
            if(not node):
                return 0
            
            res = 0
            if(gp and gp.val % 2 == 0):
                res = node.val
                
            return res + sumed(node.left, node, p) + sumed(node.right, node, p)
        
        return sumed(root, None, None)
            