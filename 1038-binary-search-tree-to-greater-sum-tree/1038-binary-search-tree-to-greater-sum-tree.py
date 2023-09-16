# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def change(node):
            nonlocal tot
            if(not node):
                return 
            
            change(node.right)
            tot += node.val
            node.val = tot
            change(node.left)
        
        tot = 0
        change(root)
        return root
            