# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverse(node, res):
            if(not node):
                return 
            
            if(not node.left and not node.right):
                res.append(node.val)
            
            traverse(node.left, res)
            traverse(node.right, res)
        
        r1 = []
        r2 = []
        traverse(root1, r1)
        traverse(root2, r2)
        return r1 == r2