# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        minCamera = [0]
        def getCoverage(root):
            if(not root):
                return 1
            
            lc = getCoverage(root.left)
            rc = getCoverage(root.right)
            if(lc == -1 or rc == -1):
                minCamera[0] += 1
                return 0
            
            if(lc == 1 and rc == 1):
                return -1
            
            if(lc == 0 or rc == 0):
                return 1
            
        lc = getCoverage(root.left)
        rc = getCoverage(root.right)
        if((lc == 1 and rc == 1) or (lc == -1 or rc == -1)):
            minCamera[0] += 1
        # getCoverage(root)
        return minCamera[0]