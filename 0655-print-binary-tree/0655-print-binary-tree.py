# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def tree_height(node):
            if(not node):
                return -1
            
            return max(tree_height(node.left),\
                       tree_height(node.right)) + 1
        
        
        def populate_tree(node, r, c):
            nonlocal height
            if(not node):
                return 
            
            tree_rep[r][c] = str(node.val)
            cr = 2 ** (height - r - 1)
            populate_tree(node.left, r + 1, c - cr)
            populate_tree(node.right, r + 1, c + cr)
            return
        
        height = tree_height(root)
        rows, cols = height + 1, (2 ** (height + 1)) - 1
        tree_rep = [([""] * cols) for _ in range(rows)]
        populate_tree(root, 0, (cols - 1) // 2)
        return tree_rep
        
        
        