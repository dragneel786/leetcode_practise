# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lsums(node, level = 0):
            nonlocal level_sums
            if not node:
                return
            
            level_sums[level] += node.val
            lsums(node.left, level + 1)
            lsums(node.right, level + 1)
        
        def assign(node, level = 0):
            if not node:
                return
            
            tot = ((node.left and node.left.val) or 0) + ((node.right and node.right.val) or 0)
            if node.left:
                node.left.val = level_sums[level + 1] - tot
            
            if node.right:
                node.right.val = level_sums[level + 1] - tot
            
            assign(node.left, level + 1)
            assign(node.right, level + 1)
        
        level_sums = Counter()
        lsums(root)
        root.val = 0
        assign(root)
        return root
        
        