# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def doTrimming(root, low, high):
            while(root):
                if(root.val < low):
                    root = root.right
                elif(root.val > high):
                    root = root.left
                else:
                    break
            
            if(not root):
                return root
                
            if(root.left):
                root.left = doTrimming(root.left, low, high)
            
            if(root.right):
                root.right = doTrimming(root.right, low, high)
            
            return root
        
        return doTrimming(root, low, high)