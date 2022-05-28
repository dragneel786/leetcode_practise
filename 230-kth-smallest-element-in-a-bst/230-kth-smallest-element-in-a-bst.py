# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int, idx = [1]) -> int:
        def findSmall(root, c):
            if(not root):
                return None
            
            ret1 = findSmall(root.left, c)
            if(ret1 != None):
                return ret1
            
            c[0] -= 1
            if(c[0] == 0):
                return root.val
            
            ret2 = findSmall(root.right, c)
            if(ret2 != None):
                return ret2
        
            return None
        
        return findSmall(root, [k])
        
        
        