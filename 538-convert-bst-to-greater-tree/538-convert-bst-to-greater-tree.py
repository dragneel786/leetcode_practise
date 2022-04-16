# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def makeGreater(root, s = [0]):
            if(not root):
                return
            
            makeGreater(root.right, s)
            root.val += s[0]
            s[0] = root.val
            makeGreater(root.left, s)
            
        
        makeGreater(root)
        return root
            