# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def getNode(root):
            nonlocal res
            if(not root):
                return
            
            if(root.val > p.val):
                res = root if(not res or root.val < res.val) else res
                getNode(root.left)
            else:
                getNode(root.right)
        
        res = None
        getNode(root)
        return res