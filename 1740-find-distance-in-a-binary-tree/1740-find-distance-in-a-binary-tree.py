# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def findLca(root):
            if(not root):
                return None
            
            if(root.val == p or root.val == q):
                return root

            left = findLca(root.left)
            right = findLca(root.right)
            if(left and right):
                return root
            
            return left if(left) else right
        
        def getDistance(root, val):
            if(not root):
                return 0

            if(root.val == val):
                return 1

            left = getDistance(root.left, val)
            if(left):
                return left + 1
            right = getDistance(root.right, val)
            if(right):
                return right + 1
            return 0
            
            
        lca = findLca(root)
        pl = 1 if(p == lca.val) else getDistance(lca, p)
        ql = 1 if(q == lca.val) else getDistance(lca, q)
        return (pl + ql - 2)
        
        
        
        