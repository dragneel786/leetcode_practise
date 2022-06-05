# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findLca(node, p, d = "S"):
            if(not node):
                return
            
            p.append(d)
            if(node.val == startValue):
                sPath[:] = p.copy()
            
            if(node.val == destValue):
                dPath[:] = p.copy()
            
            findLca(node.left, p, "L")
            findLca(node.right, p, "R")
            p.pop()
        
        sPath = [None]
        dPath = [None]
        findLca(root, [])
        while(len(sPath) and len(dPath)):
            if(sPath[0] != dPath[0]):
                break
            sPath.pop(0)
            dPath.pop(0)
        
        return "U"*len(sPath) + "".join(dPath)
