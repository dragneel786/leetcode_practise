# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def makeGreater(root, val):
            if(not root):
                return val
            
            val = makeGreater(root.right, val)
            root.val += val
            return makeGreater(root.left, root.val)
            
        
        makeGreater(root, 0)
        return root
            