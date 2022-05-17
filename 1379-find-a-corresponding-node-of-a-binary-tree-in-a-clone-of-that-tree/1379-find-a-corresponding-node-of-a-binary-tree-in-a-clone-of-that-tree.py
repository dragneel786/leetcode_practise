# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode, res = [None]) -> TreeNode:
        
        res = [None]
        
        def getRef(cloned):
            if(not cloned):
                return

            getRef(cloned.left)
            if(cloned.val == target.val):
                res[0] = cloned
                return
            getRef(cloned.right)
        
        getRef(cloned)
        return res[0]