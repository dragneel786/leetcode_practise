# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def isUni(root):
            nonlocal counts
            if(not root):
                return True
            
            left = isUni(root.left)
            right = isUni(root.right)
            if(left and right):
                if(root.left and root.left.val != root.val):
                    return False
                
                if(root.right and root.right.val != root.val):
                    return False
                
                counts += 1
                return True
            return False
        
        counts = 0
        isUni(root)
        return counts
                
                
                