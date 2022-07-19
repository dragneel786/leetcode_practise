# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def getMeClosest(root):
            nonlocal res
            if(not root):
                return
            
            if(inf == res or abs(root.val - target) < abs(target - res)):
                res = root.val
            
            if(target < root.val):
                getMeClosest(root.left)
            else:
                getMeClosest(root.right)
        
        res = inf
        getMeClosest(root)
        return res
        
        