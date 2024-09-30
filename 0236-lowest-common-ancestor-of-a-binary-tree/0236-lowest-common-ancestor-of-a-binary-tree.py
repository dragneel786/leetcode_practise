# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node):
            nonlocal lnode
            if not node:
                return False
            
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                lnode = node
                return False
            
            if (node.val == p.val or node.val == q.val) and (left or right):
                lnode = node
                return False
            
            return (node.val == p.val or node.val == q.val or left or right)
        
        lnode = None
        lca(root)
        return lnode