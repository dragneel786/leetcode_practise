# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_validity(root, lower = None, upper = None):
            if(not root):
                return True
            
            return (lower == None or lower < root.val)\
            and (upper == None or upper > root.val)\
            and check_validity(root.left, lower, root.val) \
            and check_validity(root.right, root.val, upper)
        
        return check_validity(root)
            
            
            
            
            
            
        
            
            
        
        