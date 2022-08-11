# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_validity(root):
            nonlocal prev
            if(not root):
                return True
            
            if(not check_validity(root.left) or\
               (prev != None and prev >= root.val)):
                return False
            
            prev = root.val
            return check_validity(root.right)
            
        
        prev = None
        return check_validity(root)
            
            
            
            
            
            
        
            
            
        
        