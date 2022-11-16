# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(root):
            if(not root):
                return
            
            if(not root.left and not root.right):
                yield root.val

            for v in inorder(root.left): yield v
            for v in inorder(root.right): yield v
            
        
        for a, b in itertools.zip_longest(inorder(root1), inorder(root2)):
            if(a != b):
                return False
        
        return True
        