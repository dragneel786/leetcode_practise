# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        def get_all_paths(root, op = ""):
            nonlocal res
            if(not root):
                return
            
            if(not root.left and not root.right):
                res.append(op + str(root.val))
                return
            
            val = op + str(root.val) + '->'
            get_all_paths(root.left, val)
            get_all_paths(root.right, val)
        
        res = []
        get_all_paths(root)
        return res