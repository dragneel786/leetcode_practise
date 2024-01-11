# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def find_node(node, level = 0):
            nonlocal leftmost, max_level
            if not node:
                return None
            
            find_node(node.right, level + 1)
            if(level >= max_level):
                leftmost = node
                max_level = level
            find_node(node.left, level + 1)
        
        leftmost = None
        max_level = 0
        find_node(root)
        return leftmost.val
            
        
            
            
            
            